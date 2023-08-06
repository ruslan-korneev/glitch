import click
import uvicorn

from src.services.api.app import app


@click.command("server")
@click.option("--host", default="localhost", help="on which host server will run")
@click.option("--port", default=5000, help="on which port server will run")
def run_application(host: str, port: int):
    """Run asynchronous web-application"""
    uvicorn.run(app, host=host, port=port)
