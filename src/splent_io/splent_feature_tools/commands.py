"""
CLI commands contributed by splent_feature_tools.

These commands are auto-discovered by the framework and exposed in the
SPLENT CLI under the ``feature:tools`` group.

Usage::

    splent feature:tools hello
"""

import click


@click.command("hello")
def hello():
    """Example command — replace with your own."""
    click.echo("  Hello from splent_feature_tools!")


cli_commands = [hello]
