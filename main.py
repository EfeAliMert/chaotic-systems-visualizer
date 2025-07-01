import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib
matplotlib.use('TkAgg')

# Logistic Map Formula
def logistic_map(x0, r, iterations):
    """Calculate the logistic map"""
    x_values = np.zeros(iterations)
    x_values[0] = x0
    for i in range(1, iterations):
        x_values[i] = r * x_values[i - 1] * (1 - x_values[i - 1])  # Logistic map equation
    return x_values

# Lorenz Equations
def lorenz(state, t, sigma, rho, beta):
    """Lorenz system differential equations"""
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Generate Initial Conditions from Logistic Map
def generate_initial_conditions_from_logistic(seed, r=3.9, iterations=100):
    """Generate initial conditions from logistic map"""
    logistic_values = logistic_map(seed, r, iterations)
    
    # Use the last three iteration values from logistic map to set x, y and z values
    x = logistic_values[-1] * 20  # Normalize [0, 1] -> [0, 20] range
    y = logistic_values[-2] * 20  # Normalize [0, 1] -> [0, 20] range
    z = logistic_values[-3] * 20  # Normalize [0, 1] -> [0, 20] range
    
    return [x, y, z]

# Solve Lorenz equations
def lorenz_solution(initial_state, t, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """Solve Lorenz equations and return the result"""
    return odeint(lorenz, initial_state, t, args=(sigma, rho, beta))

# Generate chaotic numbers and 3D plot
def generate_chaotic_numbers_and_3D_plot(seed, iterations, time_steps=10000):
    """Get initial conditions from logistic map and solve Lorenz equations"""
    # Get logistic map output (r=3.9) and use the last three values
    initial_state = generate_initial_conditions_from_logistic(seed, r=3.9, iterations=iterations)
    
    # Set time steps
    t = np.linspace(0, 100, time_steps)  # Adjust time range
    
    # Solve Lorenz system
    solution = lorenz_solution(initial_state, t)
    
    # Get x, y and z values from solution
    x_value = solution[-1, 0]  # x(t) value
    y_value = solution[-1, 1]  # y(t) value
    z_value = solution[-1, 2]  # z(t) value
    
    return x_value, y_value, z_value, solution, t

class LorenzVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lorenz Attractor & Logistic Map Visualizer")
        self.root.configure(bg='#f0f0f0')
        self.root.geometry("1400x900")
        
        # Animation variables
        self.animation = None
        self.current_solution = None
        self.current_t = None
        self.animation_running = False
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0', foreground='#2c3e50')
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), background='#f0f0f0', foreground='#34495e')
        style.configure('Modern.TButton', font=('Arial', 10, 'bold'), padding=10)
        style.configure('Result.TLabel', font=('Arial', 10), background='#f0f0f0', foreground='#27ae60')
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=3)
        main_frame.rowconfigure(0, weight=1)
        
        # Left panel for controls
        left_panel = ttk.Frame(main_frame, padding="10", relief="ridge")
        left_panel.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Right panel for visualization
        right_panel = ttk.Frame(main_frame, padding="10", relief="ridge")
        right_panel.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Setup left panel
        self.setup_left_panel(left_panel)
        
        # Setup right panel
        self.setup_right_panel(right_panel)
    
    def setup_left_panel(self, parent):
        # Title
        title = ttk.Label(parent, text="Scientific Visualizer", style='Title.TLabel')
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky=tk.W)
        
        # Logistic Map Section
        logistic_frame = ttk.LabelFrame(parent, text="Logistic Map Parameters", padding="15")
        logistic_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Initial value (x0)
        ttk.Label(logistic_frame, text="Initial Seed (x₀):", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=5)
        self.x0_var = tk.DoubleVar(value=0.1)
        x0_spinbox = ttk.Spinbox(logistic_frame, from_=0.001, to=0.999, textvariable=self.x0_var, width=15, increment=0.001, format="%.3f")
        x0_spinbox.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # R parameter
        ttk.Label(logistic_frame, text="Growth Rate (r):", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.r_var = tk.DoubleVar(value=3.5)
        r_spinbox = ttk.Spinbox(logistic_frame, from_=1.0, to=4.0, textvariable=self.r_var, width=15, increment=0.01, format="%.2f")
        r_spinbox.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Iterations
        ttk.Label(logistic_frame, text="Iterations:", style='Header.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.iterations_var = tk.IntVar(value=1000)
        iterations_spinbox = ttk.Spinbox(logistic_frame, from_=100, to=10000, textvariable=self.iterations_var, width=15, increment=100)
        iterations_spinbox.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Generate Logistic Map button
        logistic_btn = ttk.Button(logistic_frame, text="Generate Logistic Map", style='Modern.TButton', command=self.generate_logistic_map)
        logistic_btn.grid(row=3, column=0, columnspan=2, pady=15, sticky=(tk.W, tk.E))
        
        # Lorenz Attractor Section
        lorenz_frame = ttk.LabelFrame(parent, text="Lorenz Attractor Parameters", padding="15")
        lorenz_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Sigma parameter
        ttk.Label(lorenz_frame, text="Sigma (σ):", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=5)
        self.sigma_var = tk.DoubleVar(value=10.0)
        sigma_spinbox = ttk.Spinbox(lorenz_frame, from_=1.0, to=20.0, textvariable=self.sigma_var, width=15, increment=0.1, format="%.1f")
        sigma_spinbox.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Rho parameter
        ttk.Label(lorenz_frame, text="Rho (ρ):", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.rho_var = tk.DoubleVar(value=28.0)
        rho_spinbox = ttk.Spinbox(lorenz_frame, from_=1.0, to=50.0, textvariable=self.rho_var, width=15, increment=0.5, format="%.1f")
        rho_spinbox.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Beta parameter
        ttk.Label(lorenz_frame, text="Beta (β):", style='Header.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.beta_var = tk.DoubleVar(value=8.0/3.0)
        beta_spinbox = ttk.Spinbox(lorenz_frame, from_=0.1, to=10.0, textvariable=self.beta_var, width=15, increment=0.1, format="%.2f")
        beta_spinbox.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Time steps
        ttk.Label(lorenz_frame, text="Time Steps:", style='Header.TLabel').grid(row=3, column=0, sticky=tk.W, pady=5)
        self.time_steps_var = tk.IntVar(value=5000)
        time_steps_spinbox = ttk.Spinbox(lorenz_frame, from_=1000, to=20000, textvariable=self.time_steps_var, width=15, increment=500)
        time_steps_spinbox.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Generate Lorenz button
        lorenz_btn = ttk.Button(lorenz_frame, text="Generate Lorenz Attractor", style='Modern.TButton', command=self.generate_lorenz)
        lorenz_btn.grid(row=4, column=0, columnspan=2, pady=15, sticky=(tk.W, tk.E))
        
        # Animation Controls
        animation_frame = ttk.LabelFrame(parent, text="Animation Controls", padding="15")
        animation_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Animation buttons
        self.start_btn = ttk.Button(animation_frame, text="Start Animation", command=self.start_animation)
        self.start_btn.grid(row=0, column=0, padx=(0, 5), pady=5, sticky=(tk.W, tk.E))
        
        self.stop_btn = ttk.Button(animation_frame, text="Stop Animation", command=self.stop_animation)
        self.stop_btn.grid(row=0, column=1, padx=(5, 0), pady=5, sticky=(tk.W, tk.E))
        
        self.reset_btn = ttk.Button(animation_frame, text="Reset View", command=self.reset_view)
        self.reset_btn.grid(row=1, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Configure column weights
        animation_frame.columnconfigure(0, weight=1)
        animation_frame.columnconfigure(1, weight=1)
        
        # Results section
        results_frame = ttk.LabelFrame(parent, text="Results", padding="15")
        results_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.result_label = ttk.Label(results_frame, text="Ready to generate visualizations...", style='Result.TLabel', wraplength=280)
        self.result_label.grid(row=0, column=0, sticky=tk.W)
        
        # Configure column weights for left panel
        for frame in [logistic_frame, lorenz_frame, results_frame]:
            frame.columnconfigure(1, weight=1)
    
    def setup_right_panel(self, parent):
        # Visualization area
        viz_frame = ttk.LabelFrame(parent, text="Visualization", padding="10")
        viz_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        
        # Canvas frame - use pack geometry manager here
        self.canvas_frame = ttk.Frame(viz_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initial placeholder
        self.fig = Figure(figsize=(10, 8), dpi=100, facecolor='white')
        self.canvas = FigureCanvasTkAgg(self.fig, self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Toolbar frame
        self.toolbar_frame = ttk.Frame(viz_frame)
        self.toolbar_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Create initial empty plot
        self.ax = self.fig.add_subplot(111)
        self.ax.text(0.5, 0.5, 'Click "Generate" to start visualization', 
                    horizontalalignment='center', verticalalignment='center', 
                    transform=self.ax.transAxes, fontsize=16, color='gray')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas.draw()
    
    def generate_logistic_map(self):
        try:
            x0 = self.x0_var.get()
            r = self.r_var.get()
            iterations = self.iterations_var.get()
            
            # Validation
            if not (0 < x0 < 1):
                self.result_label.config(text="Error: Initial seed must be between 0 and 1", foreground='red')
                return
            if not (1 <= r <= 4):
                self.result_label.config(text="Error: Growth rate must be between 1 and 4", foreground='red')
                return
            if not (100 <= iterations <= 10000):
                self.result_label.config(text="Error: Iterations must be between 100 and 10000", foreground='red')
                return
            
            # Generate logistic map
            x_values = logistic_map(x0, r, iterations)
            
            # Clear and plot
            self.fig.clear()
            ax = self.fig.add_subplot(111)
            ax.plot(x_values, color='#3498db', linewidth=1.5, alpha=0.8)
            ax.set_title(f'Logistic Map (r={r}, x₀={x0})', fontsize=14, fontweight='bold', color='#2c3e50')
            ax.set_xlabel('Iterations', fontsize=12, color='#34495e')
            ax.set_ylabel('Value', fontsize=12, color='#34495e')
            ax.grid(True, alpha=0.3)
            ax.set_facecolor('#fafafa')
            
            self.canvas.draw()
            
            # Update results
            final_value = x_values[-1]
            self.result_label.config(text=f"Logistic Map completed!\nFinal value: {final_value:.6f}\nIterations: {iterations}", 
                                   foreground='#27ae60')
            
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}", foreground='red')
    
    def generate_lorenz(self):
        try:
            sigma = self.sigma_var.get()
            rho = self.rho_var.get()
            beta = self.beta_var.get()
            time_steps = self.time_steps_var.get()
            
            # Validation
            if not (1000 <= time_steps <= 20000):
                self.result_label.config(text="Error: Time steps must be between 1000 and 20000", foreground='red')
                return
            
            # Initial conditions
            initial_state = [1.0, 1.0, 1.0]
            
            # Time array
            t = np.linspace(0, 50, time_steps)
            
            # Solve differential equation
            solution = odeint(lorenz, initial_state, t, args=(sigma, rho, beta))
            
            # Store for animation
            self.current_solution = solution
            self.current_t = t
            
            # Plot static 3D graph
            self.plot_3d_graph(solution, t)
            
            # Update results
            self.result_label.config(text=f"Lorenz Attractor generated!\nσ={sigma}, ρ={rho}, β={beta:.2f}\nTime steps: {time_steps}", 
                                   foreground='#27ae60')
            
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}", foreground='red')
    
    def plot_3d_graph(self, solution, t):
        # Clear previous plot
        self.fig.clear()
        
        # Create 3D subplot
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Plot the attractor
        x, y, z = solution[:, 0], solution[:, 1], solution[:, 2]
        ax.plot(x, y, z, color='#e74c3c', linewidth=1, alpha=0.8)
        
        # Styling
        ax.set_title('Lorenz Attractor - 3D Trajectory', fontsize=14, fontweight='bold', color='#2c3e50')
        ax.set_xlabel('X', fontsize=12, color='#34495e')
        ax.set_ylabel('Y', fontsize=12, color='#34495e')
        ax.set_zlabel('Z', fontsize=12, color='#34495e')
        
        # Set background color
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        
        # Redraw canvas
        self.canvas.draw()
        
        # Create toolbar if it doesn't exist
        if not hasattr(self, 'toolbar') or self.toolbar is None:
            self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
            self.toolbar.update()
    
    def start_animation(self):
        if self.current_solution is None:
            self.result_label.config(text="Error: Generate Lorenz Attractor first!", foreground='red')
            return
        
        if self.animation_running:
            return
        
        # Stop any existing animation
        self.stop_animation()
        
        # Create animation
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        x, y, z = self.current_solution[:, 0], self.current_solution[:, 1], self.current_solution[:, 2]
        
        # Initialize empty line
        self.line, = self.ax.plot([], [], [], color='#e74c3c', linewidth=2, alpha=0.8)
        
        # Set up the axes
        self.ax.set_xlim([x.min(), x.max()])
        self.ax.set_ylim([y.min(), y.max()])
        self.ax.set_zlim([z.min(), z.max()])
        self.ax.set_title('Lorenz Attractor - Animated', fontsize=14, fontweight='bold', color='#2c3e50')
        self.ax.set_xlabel('X', fontsize=12, color='#34495e')
        self.ax.set_ylabel('Y', fontsize=12, color='#34495e')
        self.ax.set_zlabel('Z', fontsize=12, color='#34495e')
        
        # Animation function
        def animate(frame):
            if frame < len(x):
                self.line.set_data(x[:frame], y[:frame])
                self.line.set_3d_properties(z[:frame])
            return self.line,
        
        # Create and start animation
        self.animation = animation.FuncAnimation(self.fig, animate, frames=len(x), 
                                               interval=20, blit=False, repeat=True)
        self.animation_running = True
        self.canvas.draw()
        
        self.result_label.config(text="Animation started! Watch the attractor grow...", foreground='#27ae60')
    
    def stop_animation(self):
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.animation_running = False
        self.result_label.config(text="Animation stopped.", foreground='#e67e22')
    
    def reset_view(self):
        # Stop animation safely
        if self.animation is not None:
            self.animation.event_source.stop()
            self.animation = None
        self.animation_running = False
        
        # Regenerate static plot if solution exists
        if self.current_solution is not None:
            self.plot_3d_graph(self.current_solution, self.current_t)
            self.result_label.config(text="View reset to static visualization.", foreground='#3498db')
        else:
            # Clear plot
            self.fig.clear()
            self.ax = self.fig.add_subplot(111)
            self.ax.text(0.5, 0.5, 'Click "Generate" to start visualization', 
                        horizontalalignment='center', verticalalignment='center', 
                        transform=self.ax.transAxes, fontsize=16, color='gray')
            self.ax.set_xticks([])
            self.ax.set_yticks([])
            self.canvas.draw()
            self.result_label.config(text="Ready to generate visualizations...", foreground='#27ae60')

def main():
    root = tk.Tk()
    app = LorenzVisualizerApp(root)
    
    # Configure window closing
    def on_closing():
        if hasattr(app, 'animation') and app.animation is not None:
            app.animation.event_source.stop()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
