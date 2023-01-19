import os, subprocess, sys
import signal
import pyautogui


#Name and Location Variables
# projectName = input('Please enter a valid Django Project Name: ')
# appName = input('Please enter a valid Djnago App name: ')
# appFolder = input(R'Enter App location(will create a new directory in this directory): ')

projectName = 'testeroni'
appName = 'testapp'
appFolder = R'C:\Users\lug_n\OneDrive\Desktop'

settings_path = os.path.join(appFolder,projectName,projectName,'settings.py')
manage_path = os.path.join(appFolder,projectName,'manage.py')
project_dir = os.path.join(appFolder,projectName)

killcmd= pyautogui.hotkey('crtl'+'c')

#execute commands
p = subprocess.run([
    'powershell.exe',
    f'cd {appFolder}\n'
    f'mkdir {projectName}\n'
    f'cd .\{projectName}\n'
    'py -m venv env\n'
    '.\\env\\scripts\\activate\n'
    'pip install django\n'
    f'django-admin startproject {projectName} .\n'
    f'python manage.py startapp {appName}\n'
    'mkdir templates\n'
    'cd ./templates\n'
    'mkdir pages\n'
    
],stdout=sys.stdout)

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


p = subprocess.Popen([
    'powershell.exe',
    f'cd {project_dir}\n',
    killcmd,
    
],stdout=sys.stdout)
