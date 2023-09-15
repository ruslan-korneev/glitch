import click
import uvicorn

from src.services.api import application


@click.command("server")
@click.option("--host", default="0.0.0.0", help="on which host server will run")
@click.option("--port", default=5000, help="on which port server will run")
def run_application(host: str, port: int):
    """Run asynchronous web-application"""
    uvicorn.run(application, host=host, port=port)
