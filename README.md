# Introduction to Artificial Intelligence to Robotics – Resources Repository

Welcome!

This GitHub repository contains the supporting resources for NPTEL Online Course on  [Introduction to Artificial Intelligence to Robotics](https://onlinecourses.nptel.ac.in/e-learning/preview/noc26_cs183) and therefore does not provide detailed explanations of every implementation step or code segment.

The Jupyter notebooks are designed as supporting resources to help you reproduce the examples, experiment with the concepts, and reinforce your understanding. 

For comprehensive theoretical discussions, implementation details, and step-by-step explanations, please follow the weekly schedule and also earn a certificate (Videos are also available in [Youtube](https://www.youtube.com/playlist?list=PLLy_2iUCG87D-YTmxdzBKUtrOwhmwtr8G)). 

## Codes

Each week’s Jupyter notebooks are organized in separate folders and can be opened directly in Google Colab using Open in Colab.

| Weeks | Lecture Notebooks | Colab Links |
|------|----------|---------------|
| **[Week 1](./week01/)** | Lecture 4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week01/week01_lecture4.ipynb) |
| | Lecture 5 | Python Scripts provided |
| **[Week 2](./week02/)** | Lecture 6 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week02/week02_lecture6.ipynb) |
| **[Week 4](./week04/)** | Lecture 16 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week04/week04_lecture16.ipynb) |
| | Lecture 17 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week04/week04_lecture17.ipynb) |
| | Lecture 18 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week04/week04_lecture18.ipynb) |
| **[Week 7](./week07/)** | Lecture 31 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week07/week07_lecture31.ipynb) |
| | Lecture 32 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week07/week07_lecture32.ipynb) |
| | Lecture 33 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week07/week07_lecture33.ipynb) |
| | Lecture 34 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week07/week07_lecture34.ipynb) |
| | Lecture 35 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week07/week07_lecture35.ipynb) |
| **[Week 8](./week08/)** | Lecture 39 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week08/week08_lecture39.ipynb) |
| **[Week 9](./week09/)** | Lecture 43 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week09/week09_lecture43.ipynb) |
| **[Week 10](./week10/)** | Lecture 46 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week10/week10_lecture46.ipynb) |
| | Lecture 48 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week10/week10_lecture47.ipynb) |
| | Lecture 49 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week10/week10_lecture47.ipynb) |
| | Lecture 50 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/robotics-lab-iitr/nptel-ai-robotics/blob/main/week10/week10_lecture50.ipynb) |


Other week codes are *updated soon*

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
