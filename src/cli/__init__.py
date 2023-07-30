import click

from src.cli.app import run_application
from src.cli.bot import run_bot
from src.cli.db import initdb, makemigration, migrate


@click.group()
def cli():
    ...


cli.add_command(run_application)
cli.add_command(run_bot)
cli.add_command(initdb)
cli.add_command(makemigration)
cli.add_command(migrate)


__all__ = ["cli", "run_bot"]
