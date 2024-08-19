import os, subprocess
import time
from validation import validate_Name

#Name and Location Variables
pName_Condition = 0
while pName_Condition == 0:
    projectName = input('Please enter a valid Django Project Name: ').lower()
    pName_Condition = validate_Name(projectName, pName_Condition)

appName_Condition = 0        
while appName_Condition == 0:
    appName = input('Please enter a valid Djnago App name: ').lower()
    appName_Condition = validate_Name(appName, appName_Condition)
    
appFolder_Condition = 0
while appFolder_Condition == 0:    
    appFolder = input(R'Enter App location(will create a new directory in this directory): ')
    appFolder_Condition = validate_Name(appFolder, appFolder_Condition)

settings_path = os.path.join(appFolder,projectName,projectName,'settings.py')
manage_path = os.path.join(appFolder,projectName,'manage.py')
project_dir = os.path.join(appFolder,projectName)


#execute commands
p = subprocess.call([
    'powershell.exe',
    f'cd {appFolder}\n'
    f'mkdir {projectName}\n'
    f'cd .\\{projectName}\n'
    'py -m venv .venv\n'
    '.\\.venv\\scripts\\activate\n'
    'pip install django\n'
    f'django-admin startproject {projectName} .\n'
    f'python manage.py startapp {appName}\n'
    'new-item runserver.ps1\n'
    'mkdir templates\n'
    'cd ./templates\n'
    'mkdir pages\n'  
])

#Edit settings
with open(settings_path, 'r') as file:
    installed_apps = file.readlines()

installed_apps[39] = f"\n \t'{appName}'\n]"

with open(settings_path, 'w') as file:
    file.writelines( installed_apps )
    
with open(settings_path, 'r') as file:
    import_os = file.readlines()
    
import_os[13] = 'import os\n'

with open(settings_path, 'w') as file:
    file.writelines(import_os)

with open('runserver.ps1','w') as file:
    file.writelines(f'cd {project_dir}\n')
    file.writelines('.\\.venv\\scripts\\activate\n')
    file.writelines(R'python.exe .\manage.py runserver'),

script = subprocess.Popen(["powershell", "powershell -executionpolicy ByPass -File .\\runserver.ps1"])

time.sleep(5)

script.terminate()