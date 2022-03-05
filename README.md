## About ConfessionS

ConfessionS is an console diary application built with python. It's a simple non-GUI application that allow users to write any thoughts that they want at the moment, what is called a confession.  
The application has a login system, a profile with username and password must be created in order to use the app, abd all confessions created by a user can be only accessed by that user, all user info along with confessions are saved locally using _json_ files.  
The main goal of this project was/is to improve skills with python and programming in general, also putting into practice the main ideas of Human Computer Interaction, focusing on esuring usability by catching exceptions and ensuring that changes made by the user in runtime are saved. Also, the command-line resources were explored using the __rich__ library to create a good interface for the application.  

## Setup and Run

#### OS Requirements 
ConfessionS is a multiplataform application, it can run in windows and Linux default command-line interface utilitary (only tested in Windows and Ubuntu, both newer versions) as long as python is installed.  
However, because of the visual resources used such as special characters, it's recommended to use a recent version of linux terminal and use the Windows Terminal application in Windows for better experience.  

#### Setup
ConfessionS uses mostly built-in python libraries. The external libraries used are:
* [rich](https://pypi.org/project/rich/) - for visual elements of CL interface
* [cryptography](https://pypi.org/project/cryptography/) - for password ecrypting

Both can be installed with pip or conda. The __requirements.txt__ file can be used to easily install dependencies.  

##### pip installation

run `setup.sh` file or using the command below from the project's root dir.  
 
`pip install -r requirements.txt` 
 
 The shell script file creates a virtualenv named cvenv for the project.

##### running application
After dependencies are installed, the application can be launched normally with:
`python3 run.py` or `python run.py`