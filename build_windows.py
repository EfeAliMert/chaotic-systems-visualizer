#!/usr/bin/env python3
"""
Windows Build Script for Lorenz Attractor Visualizer
Run this script on a Windows machine to create Windows executable
"""

import sys
import os
import subprocess
import platform

def check_requirements():
    """Check if all required packages are installed"""
    required_packages = [
        'numpy', 'scipy', 'matplotlib', 'cx_Freeze', 'tkinter'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} is missing")
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        for package in missing_packages:
            if package == 'tkinter':
                print("tkinter comes with Python - if missing, reinstall Python")
                continue
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All packages installed!")
    
    return True

def build_windows():
    """Build Windows executable"""
    if platform.system() != 'Windows':
        print("ERROR: This script must be run on Windows!")
        print("Current system:", platform.system())
        return False
    
    print("Building Windows executable...")
    
    # Clean previous builds
    if os.path.exists('build'):
        import shutil
        print("Cleaning previous build...")
        shutil.rmtree('build')
    if os.path.exists('dist'):
        import shutil
        shutil.rmtree('dist')
    
    # Run cx_Freeze build
    result = subprocess.run([sys.executable, 'setup.py', 'build'], 
                          capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Build failed!")
        print("Error output:", result.stderr)
        return False
    
    print("Build successful!")
    
    # Find the build directory
    build_dirs = [d for d in os.listdir('build') if d.startswith('exe.win')]
    if not build_dirs:
        print("No Windows build directory found!")
        return False
    
    build_dir = os.path.join('build', build_dirs[0])
    exe_path = os.path.join(build_dir, 'LorenzAttractor.exe')
    
    if os.path.exists(exe_path):
        print(f"✓ Executable created: {exe_path}")
        
        # Create distribution folder
        dist_folder = "LorenzAttractor-Windows"
        if os.path.exists(dist_folder):
            import shutil
            shutil.rmtree(dist_folder)
        
        import shutil
        shutil.copytree(build_dir, dist_folder)
        
        # Create a launcher batch file
        with open(os.path.join(dist_folder, "run.bat"), 'w') as f:
            f.write('@echo off\n')
            f.write('cd /d "%~dp0"\n')
            f.write('LorenzAttractor.exe\n')
            f.write('pause\n')
        
        print(f"✓ Windows distribution created: {dist_folder}")
        print(f"✓ Launcher script created: {dist_folder}/run.bat")
        
        # Create README for Windows
        with open(os.path.join(dist_folder, "README.txt"), 'w') as f:
            f.write("Lorenz Attractor & Logistic Map Visualizer v3.0\n")
            f.write("=" * 50 + "\n\n")
            f.write("SYSTEM REQUIREMENTS:\n")
            f.write("- Windows 10 or later\n")
            f.write("- 64-bit architecture\n")
            f.write("- At least 4GB RAM\n\n")
            f.write("HOW TO RUN:\n")
            f.write("1. Double-click 'LorenzAttractor.exe' to run the application\n")
            f.write("2. Or double-click 'run.bat' for a console window\n\n")
            f.write("FEATURES:\n")
            f.write("- Interactive Logistic Map visualization\n")
            f.write("- 3D Lorenz Attractor with real-time animation\n")
            f.write("- Adjustable parameters for both systems\n")
            f.write("- Modern scientific computing interface\n\n")
            f.write("TROUBLESHOOTING:\n")
            f.write("- If the app doesn't start, run 'run.bat' to see error messages\n")
            f.write("- Ensure you have sufficient system memory\n")
            f.write("- Check Windows Defender if the executable is blocked\n\n")
            f.write("© 2024 Scientific Visualizer\n")
        
        return True
    else:
        print("Executable not found!")
        return False

def main():
    print("=" * 60)
    print("Lorenz Attractor Visualizer - Windows Build Script")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print()
    
    if not check_requirements():
        return 1
    
    if not build_windows():
        return 1
    
    print("\n" + "=" * 60)
    print("BUILD COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nFiles created:")
    print("- LorenzAttractor-Windows/           (Distribution folder)")
    print("- LorenzAttractor-Windows/LorenzAttractor.exe  (Main executable)")
    print("- LorenzAttractor-Windows/run.bat    (Launcher script)")
    print("- LorenzAttractor-Windows/README.txt (Instructions)")
    print("\nTo distribute: Zip the 'LorenzAttractor-Windows' folder")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 