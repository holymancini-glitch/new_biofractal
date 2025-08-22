#!/usr/bin/env python3
"""
BioFractal AI - Environment Setup and Installation Script
========================================================
Automated setup for the BioFractal AI consciousness system.
"""

import subprocess
import sys
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_command(command, description=""):
    """Run a shell command with error handling"""
    logger.info(f"Running: {description or command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        logger.info(f"Success: {description}")
        return result
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed: {description}")
        logger.error(f"Error: {e.stderr}")
        return None

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        logger.error("Python 3.8 or higher is required")
        sys.exit(1)
    logger.info(f"Python version: {sys.version}")

def create_directory_structure():
    """Create the necessary directory structure"""
    directories = [
        "modules",
        "core", 
        "data",
        "models",
        "logs",
        "exports",
        "tests",
        "configs",
        "scripts"
    ]
    
    for dir_name in directories:
        dir_path = Path(dir_name)
        dir_path.mkdir(exist_ok=True)
        
        # Create __init__.py files for Python packages
        if dir_name in ["modules", "core", "tests"]:
            init_file = dir_path / "__init__.py"
            if not init_file.exists():
                init_file.write_text('"""BioFractal AI module"""')
        
        logger.info(f"Created directory: {dir_name}")

def install_dependencies():
    """Install required dependencies"""
    logger.info("Installing Python dependencies...")
    
    # Core dependencies that should always work
    core_deps = [
        "torch>=1.12.0",
        "numpy>=1.21.0", 
        "scipy>=1.7.0",
        "matplotlib>=3.5.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "networkx>=2.6.0",
        "pydantic>=1.8.0",
        "python-dotenv>=0.19.0",
        "loguru>=0.6.0"
    ]
    
    for dep in core_deps:
        result = run_command(f"pip install {dep}", f"Installing {dep}")
        if not result:
            logger.warning(f"Failed to install {dep}, continuing...")

    # Optional advanced dependencies
    advanced_deps = [
        "brian2>=2.5.0",
        "amazon-braket-sdk>=1.30.0",
        "qiskit>=0.39.0", 
        "streamlit>=1.12.0"
    ]
    
    logger.info("Installing optional advanced dependencies...")
    for dep in advanced_deps:
        result = run_command(f"pip install {dep}", f"Installing {dep}")
        if not result:
            logger.warning(f"Optional dependency {dep} failed to install, skipping...")

def create_config_files():
    """Create default configuration files"""
    
    # Create .env file
    env_content = """# BioFractal AI Environment Configuration
DEBUG=true
LOG_LEVEL=INFO
ENABLE_GPU=true
ENABLE_QUANTUM=false
ENABLE_BIOLOGICAL=false

# AWS Configuration (optional)
# AWS_ACCESS_KEY_ID=your_key_here
# AWS_SECRET_ACCESS_KEY=your_secret_here

# Cortical Labs Configuration (optional) 
# CORTICAL_LABS_API_KEY=your_api_key_here
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    logger.info("Created .env configuration file")

def fix_import_paths():
    """Fix common import path issues"""
    logger.info("Setting up Python path...")
    
    # Add current directory to Python path
    current_dir = os.getcwd()
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

def run_basic_tests():
    """Run basic tests to verify installation"""
    logger.info("Running basic functionality tests...")
    
    try:
        import torch
        logger.info(f"✓ PyTorch {torch.__version__} installed successfully")
        
        if torch.cuda.is_available():
            logger.info(f"✓ CUDA available with {torch.cuda.device_count()} GPUs")
        else:
            logger.info("⚠ CUDA not available, using CPU")
            
    except ImportError:
        logger.error("✗ PyTorch installation failed")
    
    try:
        import numpy as np
        logger.info(f"✓ NumPy {np.__version__} installed successfully")
    except ImportError:
        logger.error("✗ NumPy installation failed")
    
    try:
        import scipy
        logger.info(f"✓ SciPy {scipy.__version__} installed successfully")
    except ImportError:
        logger.error("✗ SciPy installation failed")

def main():
    """Main setup function"""
    logger.info("🌌 BioFractal AI - Environment Setup Starting...")
    
    try:
        check_python_version()
        create_directory_structure()
        install_dependencies()
        create_config_files()
        fix_import_paths()
        run_basic_tests()
        
        logger.info("✅ Environment setup completed successfully!")
        logger.info("\nNext steps:")
        logger.info("1. Review and update the .env file with your API keys if needed")
        logger.info("2. Run: python fixed_orchestrator.py to test the system")
        logger.info("3. Check the logs/ directory for detailed logging")
        
    except Exception as e:
        logger.error(f"❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()