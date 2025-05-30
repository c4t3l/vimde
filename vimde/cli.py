# -*- coding:UTF-8 -*-

"""
Command line interface for VimDE.
"""

import getpass
import click
from vimde import utils



@click.command()
@click.option("-d", "--debug", is_flag=True, help="Start VimDE with debug logging")
@click.option("-i", "--init", is_flag=True, help="Initialize VimDE with user configurations")
@click.option("-u", "--update_plugins", is_flag=True, help="Update plugins to newest versions")
@click.option("-s", "--start", is_flag=True, default=True, help="Start VimDE. This is the default")
@click.version_option()
def main(debug, init, update_plugins, start):
    """
    VimDE is a lightweight vim+tmux based IDE. It is highly customizable and
    configurable.
    """
    utils.set_title()
    if debug:
        utils.start_vimde(debug=True)

    elif init:
        utils.init_environment()

    elif update_plugins:
        utils.install_plugins()

    else:
        utils.start_vimde()

    return click.secho(f"Bye bye. See you later {getpass.getuser()}!!", fg="cyan")


if "name" == "__main__":
    main()
