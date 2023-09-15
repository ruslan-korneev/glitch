FROM python:3.11-slim-buster

WORKDIR /app

RUN apt-get update

RUN apt-get install -y python3-pip
RUN apt-get install -y libssl-dev

COPY . .

RUN pip install -U poetry
RUN /bin/true\
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-dev \
    && rm -rf /root/.cache/pypoetry

RUN ["./entrypoint.sh"]

CMD ["poetry", "run", "glitch", "bot"]
