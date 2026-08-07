# Introduction to Artificial Intelligence to Robotics – Resources Repository

Welcome!

This GitHub repository contains the supporting resources for NPTEL Online Course on  [Introduction to Artificial Intelligence to Robotics](https://onlinecourses.nptel.ac.in/e-learning/preview/noc26_cs183) and therefore does not provide detailed explanations of every implementation step or code segment.

The Jupyter notebooks are designed as supporting resources to help you reproduce the examples, experiment with the concepts, and reinforce your understanding. 

For comprehensive theoretical discussions, implementation details, and step-by-step explanations, please follow the weekly schedule and also earn a certificate (Videos are also available in [Youtube](https://www.youtube.com/playlist?list=PLLy_2iUCG87D-YTmxdzBKUtrOwhmwtr8G)). 

## Codes

Each week's resources (Jupyter notebooks) are provided in separate folders as:

- **[Week 1](./week1/)**
- **Week 2:** _updated soon_

## Typical Workflow

1. Choose where to run the notebook (Google Colab or Local PC).
    - **Online** (Google Colab)
    - **Offline** (Local PC / Jetson Orin Nano)
2. If running in local PC / Jetson Orin Nano:
    - Install the required IDE
    - Create virtual environment using venv/conda.
    - Clone/Download the repository 
    - Open the repository folder in IDE and select the python environment
3. If running in Google Colab:
    - Open Google colab in any browser
    - Upload the notebook
    - Upload any required supporting files.
    - Execute the notebook cells.
4. Run the jupyter notebook cell-by-cell sequentially.


## VS Code IDE
 
Download and install Visual Studio Code [VS Code](https://code.visualstudio.com/Download) based on your working platform (local PC / Jetson orin nano).

```bash
# Download .deb file for arm64 device (for Jetson Orin Nano) and install using
sudo apt install code_<version_name>_arm64.deb
```

It provides:
- Excellent Jupyter Notebook support
- Integrated terminal
- Python debugging
- Git integration
- Virtual environment management

## Creating virtual environment using either **venv** or **Conda**

### Method 1 — Using venv

Download and Install [python](https://www.python.org/downloads/) (venv is preinstalled). For jetson orin nano, jetpack comes with python (venv) preinstalled. To create virtual environment, enter the following commands in terminal:

```bash
# Create a project directory
mkdir my_project

# Change into the project directory
cd my_project

# Create a virtual environment named "vrenv"
python3 -m venv vrenv

# Activate the virtual environment
source vrenv/bin/activate

# Install a package (example: rvc3python)
pip install rvc3python

# Deactivate the virtual environment after use
deactivate
```

### Method 2 — Using Conda:

Download and Install [anaconda](https://www.anaconda.com/docs/getting-started/concepts/anaconda-or-miniconda). Opt to miniconda for minimal setup. To create virtual environment, enter the following commands in anaconda prompt:
```bash
# create virtual environment with python version 3.11
conda create -n vrenv python=3.11

# Activate this environment
conda activate vrenv

# Install "rvc3python" python package in this environment
pip install rvc3python

# Deactivate the virtual environment after use
conda deactivate
```

## Python Packages 

The primary robotics library used throughout this course is Peter Corke's Robotics, Vision & Control for Python [(RVC3Python)](https://github.com/petercorke/RVC3-python). It includes NumPy, Matplotlib, SpatialMath, Robotics Toolbox, Machine Vision Toolbox, PyBullet and several other dependencies.

Additional packages required for specific lectures will be mentioned inside the corresponding notebook.

## Feedback

We will be very glad to hear from you in enhancing the repository with key and notable improvements.

Happy Learning! 🚀
