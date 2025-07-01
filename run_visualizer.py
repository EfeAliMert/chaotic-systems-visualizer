#!/usr/bin/env python3
"""
Lorenz Attractor Visualizer - Python Launcher
Direct Python execution without compilation
"""

import sys
import os
import subprocess

def main():
    print("🔬 Lorenz Attractor & Logistic Map Visualizer")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('main.py'):
        print("❌ Error: main.py not found!")
        print("Please run this script from the project directory.")
        return 1
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or later required!")
        print(f"Current version: {sys.version}")
        return 1
    
    print(f"✓ Python version: {sys.version.split()[0]}")
    
    # Check required packages
    required_packages = ['numpy', 'scipy', 'matplotlib', 'tkinter']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} available")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} missing")
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        try:
            for package in missing_packages:
                if package == 'tkinter':
                    print("⚠️  tkinter is part of Python - please reinstall Python with tkinter support")
                    continue
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print("✓ All packages installed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install packages: {e}")
            print("Please install manually: pip install numpy scipy matplotlib")
            return 1
    
    print("\n🚀 Launching Lorenz Attractor Visualizer...")
    print("-" * 50)
    
    try:
        # Launch the main application
        subprocess.run([sys.executable, 'main.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Application failed to start: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n👋 Application closed by user")
        return 0
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
