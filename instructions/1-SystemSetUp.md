## Setting up your environment 

## Goals

* Setup a development environment including:
* Configuring a python code development environment

### Github Setup
Navigate to the [Github Personal Access Tokens page](https://github.com/settings/tokens).

Click "Generate new token" on the top right. You may need to enter your Github password again.

Enter a Note for your personal access token and select the "repo" and "user:email" permissions. Click "Generate Token".

Your personal access token will be created and displayed to you. Make sure you save this token safely because it will not be shown again.


### Setting your Jenkins Administrator Password
Create a file called `jenkins-admin-password.txt` in the `jenkins\` folder. On the first line of the file type in a secure password. Save and close the file

### Docker Settings Adjustments
Open Docker Desktop by clicking on the docker icon in your Mac or Windows taskbar and selecting Dashboard. Click the gear and select "Resources" and then "Advanced". Increase the RAM allocated to docker to 4 Gigabytes. Click "Apply and Restart".

If you are running the environment on a MS Windows 10 machine, make sure to switch Docker to Linux-containers.
You can do this by clicking on the little Docker icon in your Windows taskbar.
You also need to make sure that your PC can handle virtual environments. This can be switched on or off in your systems BIOS.

### Local machine environment
For this workshop we are going to use python3 as our python, pip3 as our dependency manager, 
and virtualenv for python environment management.

First you need to fork this repo to your github account and then clone this environment to your local machine

After you install python run the following commands to start your environment
```bash
git clone https://github.com/<Your User Name>/anomaly-detection
cd <cloned repo>
docker-compose up -d --build --remove-orphans
pip3 install virtualenv
virtualenv --python=python3 .venv

# On Mac/Linux run the following
source .venv/bin/activate
pip3 install -r requirements.txt

# On Windows Powershell Run:
Set-ExecutionPolicy RemoteSigned
.venv/Scripts/activate.ps1
pip3 install -r requirements.txt
```

Note, if using PyCharm and virtualenv, be sure to select the right python interpreter for PyCharm. 
This is done by clicking on interpreter in the bottom right on the PyCharm window and 
navigating to the python3 executable in the .venv/bin/ directory. That will allow PyCharm 
to highlight missing libraries and incorrect syntax correctly. If you don't configure this 
it will show red lines everywhere because it can't find the installed libraries.


### Next Steps

Continue to the [next section](https://github.com/carlosfuentesp/anomaly-detection/instructions/2-SetupJenkins.md).