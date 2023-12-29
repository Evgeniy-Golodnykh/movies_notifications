# Movies notifications

### Description
This is a Telegram notification of the newest movies from [Radygakino theater](https://radygakino.ru). It's purpose is to simplify monitoring information about theater session.

### Quick Start
1. Clone repo
```bash
git clone git@github.com:Evgeniy-Golodnykh/movies_notifications.git
```
2. Creates the virtual environment
```bash
python3 -m venv venv
```
3. Activates the virtual environment
```bash
source venv/bin/activate
```
4. Upgrade PIP and install the requirements packages into the virtual environment
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```
5. Go to parser folder
```bash
cd parser
```
6. To run the application use command
```bash
python3 main.py
```

### Technology
[Python](https://www.python.org), [Python Telegram Bot](https://python-telegram-bot.org), [Selenium](https://selenium-python.readthedocs.io/), [SQLAlchemy](https://www.sqlalchemy.org), [PostgreSQL](https://www.postgresql.org/), [Docker](https://www.docker.com/), GitHub Actions

### Author
[Evgeniy Golodnykh](https://github.com/Evgeniy-Golodnykh)

### CI/CD pipeline status
![movies_notifications_workflow](https://github.com/Evgeniy-Golodnykh/movies_notification/actions/workflows/movies_notifications_workflow.yml/badge.svg)
