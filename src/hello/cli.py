import click


@click.command()
@click.argument("name", required=False)
def main(name: str | None = None):
    """
    Print a greeting.

    Args:
        name: Optional name to greet.
    """
    if name:
        click.echo(f"Hello, {name}!")
    else:
        click.echo("Hello, world!")
