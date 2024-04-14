## How to get started !

## Prerequisites
- Python > 3.5
- pip latest version
- git 

### NB
- The project is built on Linux Kernet | Ubuntu OS

## Steps
1. Create a directory 
```bash
mkdir <myproject>
cd <myproject>
```

2. Clone the repository
```bash
git clone https://github.com/genie360s/FlaskTemplate
```
3. Create a virtual environment
```bash
python3 -m venv .venv
```
4. Activate the virtual environment
```bash
source .venv/bin/activate
```
5. Install python packages from ```requirements.txt```
```bash
pip install -r requirements.txt
```
6. Instantiate the sqlite3 database
```bash
flask --app flaskr init-db
```
7. Run the Flask development server, with debug option
```bash
flask --app flaskr run --debug
```
8. Hooray 🚀 ! Now you are ready to get started tweaking the project.

> Created By: Alex Mkwizu @genie360s

Other documentations:
- https://flask.palletsprojects.com/en/3.0.x/tutorial/
