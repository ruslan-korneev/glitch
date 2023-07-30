import click

from src.cli.app import run_application
from src.cli.bot import run_bot


@click.group()
def cli():
    ...


cli.add_command(run_application)
cli.add_command(run_bot)


__all__ = ["cli", "run_bot"]
