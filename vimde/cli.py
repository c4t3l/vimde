# -*- coding:UTF-8 -*-

"""
Command line interface for VimDE.
"""

import getpass
import click
from vimde import utils



@click.command()
@click.option("-i", "--init", is_flag=True, help="Initialize VimDE")
@click.option("-u", "--update_plugins", is_flag=True, help="Update plugins to newest versions")
@click.option("-s", "--start", is_flag=True, default=True, help="Start VimDE. This is the default")
def main(init, update_plugins, start):
    """
    VimDE is a lightweight vim+tmux based IDE. It is highly customizable and
    configurable.
    """
    utils.set_title()
    if init:
        utils.init_environment()

    if update_plugins:
        utils.install_plugins(update=True)

    if start:
        utils.start_vimde()

    return click.secho(f"Bye bye. See you later {getpass.getuser()}!!", fg="blue")


if "name" == "__main__":
    main()
