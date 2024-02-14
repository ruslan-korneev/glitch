# GLITCH - GitLab Interface in Telegram Chat
Gitlab Assistant in telegram

- telegram bot - aiogram
- web-application - fastapi
- database - postgres
- orm -sqlalchemy

# Usage
...

# Installation
```bash
git clone git@github.com:ruslan-korneev/glitch.git
cd glitch

cat .env.example > .env
# change the values in `.env` which one do u need
```

## Locally for development
```bash
python3.11 -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install
alembic upgrade head

# commands description
glitch --help
```

## Docker
```bash
docker compose up -d --build
```
