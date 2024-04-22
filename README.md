# Django First project (SQLite db)

### 1. Create virtual environment and install packages
Windows
```shell
python -m venv venv && venv\Scripts\activate && python -m pip install -r requirements.txt && python manage.py migrate && python manage.py createsuperuser 
```

Linux/Mac
```shell
python3 -m venv venv && source venv/bin/activate && python3 -m install -r requirements.txt  && python3 manage.py migrate && python3 manage.py createsuperuser 
```

### 2. Create .env file and copy all variables from .env_example to it and customize your self (if needed)

### 3. Run django project
Windows
```shell
python manage.py runserver
```
Linux/Mac
```shell
python3 manage.py runserver
```
