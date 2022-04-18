# method 1 using the terminal
# to check you have python
firstcommand= 'python --version'
# to check pip
secondcommand= 'pip -V'
# to install Tkinter
thirdcommand= 'pip install tk'

# Method 2
from setuptools import setup

setup(
    name="tkinter",
    version="(8.6. 12",
    description = "  Python's de-facto standard GUI (Graphical User Interface) package",
    author =" Steen Lumholt and Guido van Rossum revised by  Fredrik Lundh",
    packages=['tkinter'],
    install_requirements="python"

)