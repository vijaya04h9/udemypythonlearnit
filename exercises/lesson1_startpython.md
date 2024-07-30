# Python Development Environment Setup

Welcome, Python developer. This guide will walk you through setting up a comprehensive Python development environment, including core tools, version control, and IDEs. Follow these units to create an optimal workspace for your Python projects.

## Unit 1: Core Python Setup

### Task 1.1: Install Python

1. Visit the official [Python Downloads](https://www.python.org/downloads/) page.
2. Download the latest stable Python release (currently Python 3.12.2, but check for updates).
3. Run the installer with admin rights, making sure to check "Add python.exe to PATH".
4. Complete the installation with the recommended settings.

### Task 1.2: Verify Python Installation

1. Open a terminal (Command Prompt for Windows, Terminal for macOS/Linux).
2. Run the following command to check the Python version:
   ```
   python --version
   ```
3. Ensure the output matches the version you installed. If not, revisit Task 1.1.

### Task 1.3: Explore the Python REPL

1. In the terminal, start the Python REPL by typing: `python`
2. Try out some Python commands:
   - `print("Hello, Python!")`
   - `import sys; print(sys.version)`
   - `exit()` to close the REPL

## Unit 2: Version Control Setup

### Task 2.1: Install Git

1. Go to the official [Git Downloads](https://git-scm.com/downloads) page.
2. Download the appropriate version for your operating system.
3. Run the installer, accepting the default options (you can customize if you're familiar with Git).
4. During installation, ensure that "Git Bash Here" and "Git GUI Here" options are selected for easy access.
5. Choose to use Git from the Windows Command Prompt (Windows-specific option).

### Task 2.2: Verify Git Installation

1. Open a new terminal window (to ensure PATH updates take effect).
2. Run the following command to check the Git version:
   ```
   git --version
   ```
3. If you see a version number, Git is successfully installed. If not, try restarting your computer or revisit Task 2.1.

## Unit 3: IDE Setup

### Task 3.1: Install and Configure Your IDE

#### Option A: PyCharm (Popular for Python-specific development)

1. Go to the [PyCharm download](https://www.jetbrains.com/pycharm/download/) page.
2. Choose and download the Community Edition for your OS.
3. During installation, select "Create Desktop Shortcut" and "Update PATH variable".

#### Option B: Visual Studio Code (Great for multi-language projects)

1. Visit the [Visual Studio Code](https://code.visualstudio.com/download) download page.
2. Download and install VS Code, selecting "Add to PATH" during setup.
3. After installation, open VS Code and install the Python extension from the marketplace.

## Unit 4: Project Setup

### Task 4.1: Clone the Course Repository

1. Open your terminal and navigate to your projects directory.
2. Clone the course repository with this Git command:
   ```
   git clone https://github.com/learnitlessons/pythonlearnit.git
   ```
3. Move into the cloned directory: `cd pythonlearnit`
4. Check the contents with `dir` (Windows) or `ls` (macOS/Linux).

### Task 4.2: Configure Project in IDE

1. From your project directory in the terminal:
   - For PyCharm: `pycharm .`
   - For VS Code: `code .`
2. Set up your project interpreter and ensure Git is properly integrated.

## Alternative: Cloud Development Environments

If you need to start coding quickly or prefer cloud-based environments, consider these options:

- [Jupyter Notebook](https://jupyter.org/try): Great for data analysis and interactive Python development.
- [Google Colab](https://colab.research.google.com/): Jupyter notebooks with free GPU access (requires Google account).
- [GitHub Codespaces](https://github.com/codespaces): Full VS Code experience in the cloud (requires GitHub account).

Congratulations! You've completed the setup of your Python development environment, including core tools, version control, and IDE configuration. You're now ready to start coding your Python projects. Happy coding!