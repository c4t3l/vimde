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


def _lockfile(create=False):
    """
    Check if lockfile exists. If "create=True" is passed, then create the lockfile.
    """
    lock = pathlib.Path.home().joinpath('.vimde/LockFile')

    if create:
        pathlib.Path.touch(lock)
    return lock.exists()


def die(msg, color=None):
    """
    Kills execution of the program.  Also prints a nice message for the user.
    """
    secho(msg, fg=color)
    return sys.exit(1)


def init_environment():
    """
    Creates the $HOME/.vimde and $HOME/.tmuxde dirs.
    This function is destructive to user vimderc and tmuxderc if LockFile
    does not exist.
    """
    import pudb; pu.db
    if _lockfile():
        die('[WARNING] ~/.vimde/LockFile exists!!  Cowardly refusing to ' \
            're-initialize environment.', color='yellow')

    vimde_dir = pathlib.Path.home().joinpath('.vimde')
    tmuxde_dir = pathlib.Path.home().joinpath('.tmuxde')
    vimde_dir.mkdir(exist_ok=True)
    tmuxde_dir.mkdir(exist_ok=True)

    for app in ["tmuxderc", "vimderc"]:
        if copy_configs(app):
            install_plugins()
   
    # Protect the user plugins/configuration data
    return _lockfile(create=True), secho('[INFO] VimDE environment initialized. Please restart VimDE.',
                 color='yellow')


def copy_configs(app): 
    """
    Copy system config files to the user home directory
    'app' can be either "vimderc" or "tmuxderc"
    The operation is destructive to user config path, be sure to
    set _lockfile to protect.
    """

    app_global = pathlib.Path().joinpath('/etc/vimde/' + app)
    app_local = pathlib.Path.home().joinpath('.' + app)

    return shutil.copy(app_global, app_local)


def install_plugins(update=False):
    """
    Installs base set of Vundle plugins to local user account.
    This relies on provided plugins from /usr/share/vimde/bundle.
    The operation is destructive to user plugin path, be sure to
    set _lockfile to proctect.

    vim +PluginInstall +qall
    """
    if update:
        cmd = f"vim -u {str(get_config('vimderc'))} +PluginInstall +qall"
        cmd = shlex.split(cmd)
        return _run(cmd)
    
    global_vim_plugins_path = pathlib.Path('/usr/share/vimde/bundle')
    user_vim_plugins_path = pathlib.Path.home().joinpath('.vimde/bundle')

    global_tmux_plugins_path = pathlib.Path('/usr/share/tmuxde/plugins')
    user_tmux_plugins_path = pathlib.Path.home().joinpath('.tmuxde/plugins')

    shutil.rmtree(user_vim_plugins_path, ignore_errors=True)
    shutil.rmtree(user_tmux_plugins_path, ignore_errors=True)

    vim_copy = shutil.copytree(global_vim_plugins_path, user_vim_plugins_path)
    tmux_copy = shutil.copytree(global_tmux_plugins_path, user_tmux_plugins_path)
    return vim_copy, tmux_copy


def get_config(app):
    """
    If user config detected it will override
    the systemwide config

    Accepts three (1) arg
    :app: str (vimderc|tmuxderc)
    """

    app_global = pathlib.Path().joinpath('/etc/vimde/' + app)
    app_local = pathlib.Path.home().joinpath('.' + app)

    # If global configs dont exist we have a major problem
    if not app_global.exists():
        die(f"[ERROR] Filepath: {app_global.absolute()} is missing!! Aborting startup.", color="red")

    return app_local.absolute() if app_local.exists() else app_global.absolute()

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
