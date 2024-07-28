import click
# from utils import Settings

@click.group()
def cli():
    """"""
    pass

@cli.group()
def config():
    pass

@cli.group()
def project():
    """"""
    pass

@project.command()
def start():
    """"""
    print("Motherfucker")

@project.command()
def remove():
    """"""
    click.echo("remove")

@project.group()
def edit():
    pass

@edit.command()
@click.argument('autoupdate')
def auto_update(autoupdate: bool = True):
    """"""
    pass

if __name__ == '__main__':
    if Settings.check_config_file():
        print('here')
    else:
        print('there')
    cli()


