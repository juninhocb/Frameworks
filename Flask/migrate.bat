@echo off
REM run db init just if is the first time running this .bat
flask --app app\main db init  
flask --app app\main db migrate
flask --app app\main db upgrade
