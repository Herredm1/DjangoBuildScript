# DjangoBuildScript
Builds a barebones Django APP in seconds. 

# Python Script Summary

This script automates the setup and configuration of a Django project and app, including the creation of a virtual environment, installation of required packages, and modification of Django's settings.

## Overview

1. **Import Modules:**
   - Imports necessary Python modules: `os`, `subprocess`, `time`, and a custom `validate_Name` function from the `validation` module.

2. **Project and App Naming:**
   - Prompts the user to input a valid Django project name, Django app name, and app location.
   - Uses the `validate_Name` function to ensure the provided names are valid.

3. **Path Setup:**
   - Constructs paths for the Django project's `settings.py`, `manage.py`, project directory, and `.env` file based on user input.

4. **Execution of Commands:**
   - Runs a series of PowerShell commands to:
     - Create the project directory.
     - Set up a Python virtual environment.
     - Install Django and `python-dotenv`.
     - Create a new Django project and app.
     - Set up basic project structure including directories for templates and static files.
     - Generate a `.env` file for environment variables.

5. **Write to `.env` File:**
   - Writes the `api_key` to the `.env` file.

6. **Modify `settings.py`:**
   - Opens the `settings.py` file and modifies it to:
     - Import `os` and `load_dotenv`.
     - Load the `SECRET_KEY` from the `.env` file.
     - Add the app name to the `INSTALLED_APPS` list.
     - Set the `STATICFILES_DIRS` to include the static directory.
     - Set the `DIRS` in the `TEMPLATES` setting to include the templates directory.

7. **Create `runserver.ps1`:**
   - Generates a PowerShell script `runserver.ps1` that:
     - Activates the virtual environment.
     - Runs the Django development server.

8. **Run the Django Server:**
   - Executes the `runserver.ps1` script to start the Django development server.
   - The script waits for 5 seconds before terminating the server.

## Conclusion

This script streamlines the setup process for a Django project by automating the creation and configuration of necessary files and directories. It also sets up a basic development environment with a PowerShell script to run the Django server. Feel free to make changes and if you have recommendations please let me know.
