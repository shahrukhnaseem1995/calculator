@echo off
echo === Activating Virtual Environment ===
call venv\Scripts\activate

echo === Installing Requirements ===
pip install -r requirements.txt

echo === Running Tests with Coverage ===
pytest --cov=calculator --cov-report=term-missing --cov-report=html

echo === Opening Coverage Report ===
start htmlcov\index.html

echo === Done ===
pause
