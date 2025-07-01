# Lorenz Attractor & Logistic Map Visualizer v3.0

Scientific visualization tool for exploring chaotic dynamical systems including the famous Lorenz Attractor and Logistic Map with real-time animation capabilities.

![Version](https://img.shields.io/badge/version-3.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-green)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)

## ✨ Features

### 🌪️ **Lorenz Attractor**
- **3D Visualization**: Interactive 3D plotting of the chaotic Lorenz system
- **Real-time Animation**: Watch the attractor grow dynamically with smooth animations
- **Parameter Control**: Adjust σ (sigma), ρ (rho), and β (beta) parameters in real-time
- **High-quality Rendering**: Anti-aliased graphics with professional styling

### 📈 **Logistic Map**
- **2D Visualization**: Clear plotting of population dynamics
- **Parameter Exploration**: Investigate chaos through growth rate (r) variations
- **Bifurcation Analysis**: Observe period-doubling routes to chaos
- **Interactive Controls**: Real-time parameter adjustment with instant feedback

### 🎛️ **Modern Interface**
- **Professional Design**: Clean, modern GUI with scientific aesthetics
- **Responsive Layout**: Adaptive interface that works on different screen sizes
- **Animation Controls**: Start, stop, and reset animations with dedicated buttons
- **Parameter Validation**: Built-in validation prevents invalid input ranges
- **Real-time Feedback**: Instant results display and error messaging

## 📦 Downloads

### Windows
- **Script**: `build_windows.py`
- **Requirements**: Windows 10 or later, Python 3.8+
- **Build Instructions**:
  1. Install Python 3.8+ from [python.org](https://python.org)
  2. Download all project files to a folder
  3. Open Command Prompt in that folder
  4. Run: `python build_windows.py`
  5. Find executable in `LorenzAttractor-Windows` folder

## 🔧 Building from Source

### Prerequisites
```bash
pip install numpy scipy matplotlib cx_Freeze
```

### For Windows:
```bash
python build_windows.py
```

## 🎯 Usage Guide

### Logistic Map Exploration
1. **Initial Seed (x₀)**: Set between 0.001 and 0.999
2. **Growth Rate (r)**: Explore values from 1.0 to 4.0
   - r < 1: Population dies out
   - 1 < r < 3: Stable population
   - 3 < r < ~3.57: Oscillating behavior
   - r > ~3.57: Chaotic dynamics
3. **Iterations**: Number of population cycles (100-10,000)

### Lorenz Attractor Parameters
1. **Sigma (σ)**: Controls the rate of rotation (1.0-20.0)
2. **Rho (ρ)**: Related to Rayleigh number (1.0-50.0)
3. **Beta (β)**: Geometric factor (0.1-10.0)
4. **Time Steps**: Simulation resolution (1,000-20,000)

**Classic Chaotic Values**: σ=10, ρ=28, β=8/3

### Animation Features
- **Start Animation**: Watch the attractor grow point by point
- **Stop Animation**: Pause the current animation
- **Reset View**: Return to static complete visualization

## 🔬 Scientific Background

### Lorenz System
Discovered by Edward Lorenz in 1963, this system demonstrates sensitive dependence on initial conditions - the "butterfly effect." The equations are:

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y  
dz/dt = xy - βz
```

### Logistic Map
A discrete-time dynamical system that models population growth:

```
xₙ₊₁ = r·xₙ(1 - xₙ)
```

This simple equation exhibits incredibly complex behavior including period-doubling bifurcations and chaos.

## 🛠️ Technical Details

### Built With
- **Python 3.8+**: Core language
- **NumPy**: Numerical computations
- **SciPy**: ODE integration (Lorenz system)
- **Matplotlib**: Scientific plotting and animation
- **Tkinter**: Cross-platform GUI framework
- **cx_Freeze**: Executable packaging

### Performance
- **Memory Usage**: ~200-400 MB during animation
- **CPU Usage**: Optimized for real-time performance
- **Graphics**: Hardware-accelerated rendering when available

### Compatibility
- **Windows**: 10/11 (64-bit)
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

## 🐛 Troubleshooting

### Common Issues

**Windows: "Windows protected your PC"**
- Click "More info" → "Run anyway"

**Animation runs slowly**
- Reduce time steps parameter
- Close other applications
- Check available system memory

**Parameters reset unexpectedly**
- Ensure values are within valid ranges
- Check for decimal separator (use . not ,)

### System Requirements
- **RAM**: Minimum 4GB, recommended 8GB+
- **Storage**: 200MB free space
- **Graphics**: Integrated graphics sufficient

## 📚 Educational Use

This software is perfect for:
- **Physics Courses**: Demonstrating nonlinear dynamics
- **Mathematics**: Exploring chaos theory and bifurcations
- **Computer Science**: Understanding numerical methods
- **Research**: Parameter space exploration

## 🤝 Contributing

This is an educational project. For improvements or bug reports:
1. Document the issue clearly
2. Include system information
3. Provide steps to reproduce


## 🙏 Acknowledgments

- **Edward Lorenz**: For discovering the Lorenz system
- **Robert May**: For popularizing the logistic map
- **Scientific Python Community**: For excellent libraries
- **Matplotlib Team**: For powerful visualization tools
**Explore the beauty of chaos theory with interactive mathematical visualizations!**

