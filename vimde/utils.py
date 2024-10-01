# -*- coding: UTF-8 -*-

"""
Vimde utilities module.
"""

import pathlib
import sys
import shlex
import shutil
import subprocess
import setproctitle
from click import secho


def die(msg, color=None):
    """
    Kills execution of the program.  Also prints a nice message for the user.
    """
    secho(msg, fg=color)
    sys.exit(1)


def init_environment():
    """
    Creates the $HOME/.vimde and $HOME/.tmuxde dirs.
    """
    vimde_dir = pathlib.Path.home().joinpath('.vimde')
    tmuxde_dir = pathlib.Path.home().joinpath('.tmuxde')
    vimde_dir.mkdir(exist_ok=True)
    tmuxde_dir.mkdir(exist_ok=True)

    if copy_configs():
        copy_plugins()
        install_plugins()
        secho('[INFO] VimDE environment initialized. Please restart VimDE.',
                color='yellow')


def copy_configs():
    """
    Copy system config files to the user home directory
    """
    global_vimderc = get_config('vimderc', system=True)
    global_tmuxderc = get_config('tmuxderc', system=True)
    local_vimderc = get_config('vimderc', local=True)
    local_tmuxderc = get_config('tmuxderc', local=True)
    shutil.copy(global_vimderc, local_vimderc)
    shutil.copy(global_tmuxderc, local_tmuxderc)

    if not (pathlib.Path.exists(local_vimderc)
            and pathlib.Path.exists(local_tmuxderc)):
        die('[ERROR] Configuration file copy failed. ' \
            'Please rerun "vimde --init".', color='red')


def copy_plugins():
    """
    Copies plugins from base install path to user path.
    """

    system_vim_plugins_path = pathlib.Path('/usr/share/vimde/bundle')
    user_vim_plugins_path = pathlib.Path.home().joinpath('.vimde/bundle')
    system_tmux_plugins_path = pathlib.Path('/usr/share/tmuxde/plugins')
    user_tmux_plugins_path = pathlib.Path.home().joinpath('.tmuxde/plugins')

    shutil.rmtree(user_vim_plugins_path, ignore_errors=True)
    shutil.rmtree(user_tmux_plugins_path, ignore_errors=True)
    vim_copy = shutil.copytree(system_vim_plugins_path, user_vim_plugins_path)
    tmux_copy = shutil.copytree(system_tmux_plugins_path, user_tmux_plugins_path)
    return vim_copy, tmux_copy


def install_plugins(update=False):
    """
    Installs base set of Vundle plugins to local user account.
    This relies on provided plugins from /usr/share/vimde/bundle.

    vim +PluginInstall +qall
    """
    if update:
        if not _lockfile():
            die('[ERROR] VimDE is not initialized.  Please run "vimde --init" ' \
                'to initialize your environment.', color='red')
        cmd = f'vim -u  {str(get_config("vimderc"))} +PluginUpdate +qall'

    else:
        cmd = f'vim -u {str(get_config("vimderc"))} +PluginInstall +qall'

    cmd = shlex.split(cmd)
    return _run(cmd)


def get_config(app):
    import pudb;pu.db
    """
    If user config detected it will override
    the systemwide config

    Accepts three (1) arg
    :app: str (vimderc|tmuxderc)
    """

    app_global = pathlib.Path(f"/etc/vimde/{app}")
    app_local = pathlib.Path.home().joinpath(f".{app}")

    # if local:
    #     return app_local.absolute()

    # if system:
    #     return app_global.absolute()

    # if app_local.exists():
    #     return app_local.absolute()

    # return app_global.absolute()


def set_title():
    """Set the process title for ps output"""
    setproctitle.setproctitle('vimde')


def _run(*args):
    """
    Executes passed code.  Basically a passthrough for subprocess.
    """

    # Basic arg validation
    my_args = args[0]
    if not isinstance(my_args, list):
        sys.stderr.write(f'dumping args: {my_args}\n')
        return die('[ERROR] passed badly formatted list to _run.', color='red')

    return subprocess.run(my_args, check=True)


def start_vimde(debug=False):
    """
    Handles startup of the application.
    """

    if debug:
        cmd = f'tmux -f {str(get_config("tmuxderc"))} new-session -s VimDE_DEBUG-MODE ' \
              f'vim -u {str(get_config("vimderc"))} -V9{pathlib.Path.home().joinpath(".vimde", "debug.log")}'
        cmd = shlex.split(cmd)

    else:
        cmd = f'tmux -f {str(get_config("tmuxderc"))} new-session -s VimDE ' \
              f'vim -u {str(get_config("vimderc"))}'
        cmd = shlex.split(cmd)
    return _run(cmd)
