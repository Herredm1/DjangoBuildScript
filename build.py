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
env_path = os.path.join(project_dir, '.venv','.env')


#execute commands
p = subprocess.call([
    'powershell.exe',
    f'cd {appFolder}\n'
    f'mkdir {projectName}\n'
    f'cd .\\{projectName}\n'
    'py -m venv .venv\n'
    '.\\.venv\\scripts\\activate\n'
    'pip install django, python-dotenv\n'
    f'django-admin startproject {projectName} .\n'
    f'python manage.py startapp {appName}\n'
    'new-item runserver.ps1\n'
    'mkdir templates\n'
    'cd ./templates\n'
    'new-item base.html\n'
    'mkdir pages\n'
    'cd ../\n'
    'mkdir static\n'
    'cd static\n'
    'mkdir js, css, images\n'
    'cd ../.venv\n'
    'new-item .env\n'  
])

#Edit settings

with open(settings_path, 'r') as file:
    lines = file.readlines()  # Read the entire file into a list

# Modify specific lines

api_key = str(lines[22])[13::]

static_content = "STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n"
lines[118] = static_content

dir_content = "\n \t \t'DIRS': {os.path.join(BASE_DIR, 'templates')},\n"
lines[56] = dir_content

app_content = f"\t'{appName}'\n]"
lines[39] = app_content

django_secret=  "SECRET_KEY = api_key"
lines[22] = django_secret

os_content = "import os\nfrom dotenv import load_dotenv\nload_dotenv()\napi_key=os.getenv('api_key')"
lines[13] = os_content



    
# Write the modified lines back to the file
with open(settings_path, 'w') as file:
    file.writelines(lines)
    
with open(env_path, 'w') as env:
    env.write(f'api_key={api_key}')

with open('runserver.ps1','w') as file:
    file.writelines(f'cd {project_dir}\n')
    file.writelines('.\\.venv\\scripts\\activate\n')
    file.writelines(R'python.exe .\manage.py runserver'),

script = subprocess.Popen(["powershell", "powershell -executionpolicy ByPass -File .\\runserver.ps1"])

time.sleep(5)

script.terminate()