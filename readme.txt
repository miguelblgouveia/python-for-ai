#Primeiro é necessário dar permissões de execução ao script para ativação do ambiente virtual
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; & D:/dev/PythonProjects/python-for-ai/.venv/Scripts/Activate.ps1 

# Depois, instalar a biblioteca requests
py -m pip install requests

# instalar o ipykernel para permitir execução de células interativas no VS Code
py -m pip install ipykernel

# Depois nos setings do VS Code ativar:
Jupyter > interactive window > Text Editor: Execute Selection

# Instalar requirements
py -m pip install -r requirements.txt

# para criar o arquivo requirements.txt
py -m pip freeze > requirements.txt

# instalar matplotlib
py -m pip install matplotlib

# Instalar openpyxl para manipulação de arquivos Excel
py -m pip install openpyxl