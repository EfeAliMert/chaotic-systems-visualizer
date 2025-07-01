import sys
from cx_Freeze import setup, Executable

# Cross-platform dependencies and libraries
build_exe_options = {
    "packages": [
        "numpy", 
        "scipy", 
        "matplotlib", 
        "tkinter", 
        "unittest",
        "PIL",  # For better image support
        "matplotlib.backends.backend_tkagg"
    ],
    "includes": [
        "tkinter.ttk",
        "matplotlib.figure",
        "matplotlib.animation",
        "matplotlib.backends._backend_tk"
    ],
    "excludes": [
        "test",
        "distutils",
        "email",
        "pydoc_data",
        "unittest.test"
    ],
    "include_files": [
        # Include matplotlib data
    ],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
}

# Platform-specific base settings
base = None
target_name = "LorenzAttractor"

if sys.platform == "win32":
    base = "Win32GUI"  # Windows GUI app (no console)
    target_name = "LorenzAttractor.exe"
    # Windows specific options
    build_exe_options["include_msvcrt"] = True
elif sys.platform == "darwin":  # macOS
    base = None  # Mac için None kullanılır
    # Mac specific options - no special requirements

# Create the executable configuration
executable = Executable(
    "main.py", 
    base=base, 
    target_name=target_name,
    icon=None,  # Add .ico file path here if you have an icon
    shortcut_name="Lorenz Attractor Visualizer",
    shortcut_dir="DesktopFolder",
)

setup(
    name="LorenzAttractor",
    version="3.0",
    author="Scientific Visualizer",
    description="Lorenz Attractor & Logistic Map Visualizer - Modern Scientific Computing Tool",
    long_description="A modern scientific visualization tool for exploring chaotic systems including the Lorenz Attractor and Logistic Map with real-time animation capabilities.",
    options={"build_exe": build_exe_options},
    executables=[executable],
)
