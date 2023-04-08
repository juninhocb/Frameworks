@echo off
python -m venv venv
Set-ExecutionPolicy RemoteSigned
venv\Scripts\activate.bat
pip install -r requirements.txt
