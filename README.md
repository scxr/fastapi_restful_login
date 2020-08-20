# What is this
This is a secure rest login system created with FastAPI by [cswil](https://github.com/cswil) that uses bcrypt and sqlalchemy.

## How to run

install dependencies located in requirements.txt then execute main.py

## How to use

You can use http://127.0.0.1:5000/docs to see the gui that fastapi spins up for you, which I only really used to generate curl commmands and did not take the time to understand what it all means because, ew, GUIS :)

However, there is two endpoints which are intuitively register and login. Register expects username and password in request as does login, which im sure you can figure out by reading the code. I plan to clean the code up later on, putting it in src folders etc, however this is my first fastapi project so have yet to figure out the correct anatomy of a fastapi project though from looking it doesnt seem to differ from Flask. 
