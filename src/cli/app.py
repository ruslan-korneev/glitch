import click
import uvicorn
from fastapi import FastAPI


@click.command("server")
@click.option("--host", default="localhost", help="on which host server will run")
@click.option("--port", default=5000, help="on which port server will run")
def run_application(host: str, port: int):
    """Run asynchronous web-application"""
    app = FastAPI()
    uvicorn.run(app, host=host, port=port)
