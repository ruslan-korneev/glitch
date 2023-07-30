# GLITCH - GitLab Interface in Telegram Chat
Version Control System via telegram, written in python

- telegram bot - aiogram
- web-application - fastapi
- database - postgres
- orm -sqlalchemy

# Usage
...

# Installation
```bash
git clone git@github.com:ruslan-korneev/gitlab-tg-interface.git
cd gitlab-tg-interface

cat env_sample > .env
# change the values in `.env` which one do u need
```

## Locally for development
```bash
python3.11 -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install

# commands description
glitch --help
```

## Docker
```bash
docker compose up -d --build
```
