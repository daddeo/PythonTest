import sys

print("testing")

print("ver: ", sys.version)
print("exe: ", sys.executable)

# --------------------------------------------------------------------------------------
# useful commands
#
# pip list -- shows all packagages installed
#
# use virtual envrionment to separate development environments (e.g. packages, version),
# otherwise uses the global environment making things harder to use differing package versions
# and such.
# from command prompt:
# python -m venv {name}, e.g. name = project_env
# (to active new venv name):
# {name}\scripts\activate.bat
#
# ex:
# c:\>mkdir my_project
# c:\>python -m venv my_project\venv
# c:\>my_project\venv\Scripts\activate.bat
#
# output:
# (venv) c:\>
#
# 'where python', gives the paths to the current python command
# will show the venv path and the python path
#
# {requirements.txt} file contents gotten from 'pip freeze'
# this can be used by another person to get all the packages you are using.
#
# ex (while in venv):
# pip install -r {requirements.txt}
#
# NOTE: DO NOT PUT folders or files in the venv directory!
# NOTE: Add /venv directory to the .gitignore file
# NOTE: commit {requirements.txt} to source control so others can build your project
#
# to get rid of an venv
# 1. open command prompt (navigate to the directory)
# 2. deactivate
# 3. (optional) delete the environment, from command prompt of the directory owning the
#   environment... rmdir {name} /s
#
#
# to show only the packages that we have installed (not including system ones), use
# pip list --local
#
# also works for freeze
# pip freeze -- local
#
#
#
# using GIT Bash for terminal
# 'clear' ~ 'cls'
# git config --list
# git config --global user.name "{name}" -- name: daddeo
# git config --global user.email "{email}" -- email: gmail
#
