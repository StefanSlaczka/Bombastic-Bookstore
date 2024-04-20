@echo off

REM 1. Clone the repository
git clone https://github.com/Volatar/Bombastic-Bookstore

REM 2. Create and activate the virtual environment
python -m venv Virtualenv
call Virtualenv\Scripts\activate

REM 3. Install dependencies
pip install -r Bombastic-Bookstore\requirements.txt

REM 4. Run the project
cd Bombastic-Bookstore
start "" cmd /c "flask run"

REM 5. Wait for Flask server to start
timeout /t 5

REM 6. Opens browser
start "" chrome http://127.0.0.1:5000



