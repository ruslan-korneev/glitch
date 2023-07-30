import click


@click.command("initdb")
def initdb():
    """Initializing database"""
    click.echo("Initializing database ...")


@click.command("makemigration")
def makemigration():
    """Create new version of database schema"""
    click.echo("Create new version of database schema")


@click.command("migrate")
@click.argument("version", required=False, type=str)
def migrate():
    """Applying certain version of schema to database"""
    click.echo("Applying certain version of schema to database ...")
