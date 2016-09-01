import os
import click
from flask.cli import FlaskGroup

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


def create_application(info):
    from app import create_app
    return create_app()


@click.group(cls=FlaskGroup, create_app=create_application)
def cli():
    """This is a management script for the bill flexor application."""
    pass


@cli.command()
def test():
    """Runs unit tests"""
    import pytest
    click.echo('Running tests')
    pytest.main(['-x', 'tests'])
    if COV:
        COV.stop()
        COV.save()
        click.echo('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        click.echo('HTML version: file://%s/index.html' % covdir)
        COV.erase()


@cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')


if __name__ == '__main__':
    cli()
