import click

from pathlib import Path


class GlobalOptions:
    def __init__(self):
        self.verbosity = 0


pass_global_opts = click.make_pass_decorator(GlobalOptions, ensure=True)


def verbosity_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(GlobalOptions)
        state.verbosity = value
        return value

    return click.option("--verbose", "-v",
                        count=True, expose_value=False, help="Enables verbosity.", callback=callback)(f)


def global_options(f):
    f = verbosity_option(f)
    return f


@click.group(
    help="Kubernetes native development and deploy management",
)
def factory() -> None:
    pass


@factory.command()
@click.argument(
    "target",
    type=str
)
def make(target: str) -> None:
    click.echo("factory.make: {}".format(target))


@factory.command(
    help="Proxy traffic between your local project and a remote Kubernetes environment"
)
@click.option(
    "--shell",
)
@click.option(
    "--swap"
)
def meld(shell: True) -> None:
    click.echo("factory.meld")


@factory.command(
    help="Initialize a new Factory project",
)
@click.option(
    "--name",
    help="Set the project name",
    type=str,
)
@click.option(
    "--path",
    help="Set the project path",
    type=click.Path(),
    default=str(Path.cwd())
)
def init(path: str) -> None:
    click.echo("factory.init: {}".format(path))
