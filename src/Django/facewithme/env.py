import os
import sys

# setup pythonpath - add ./lib before any others paths
# overwrite django and other shared python libs
# it's one of 'little ugly hack' that make things works
__root = os.path.dirname(os.path.abspath(__file__))
__path = lambda *a: os.path.join(__root, *a)
if os.path.exists(__path('lib')):
    sys.path.insert(0, __path('lib'))
sys.path.insert(0, __path(''))
del __root, __path


def setup(root=None, settings_module_name=None):
    """
    Simple setup snippet that makes easy to create
    fast sandbox to try new things.

    :param root: the root of your project
    :param settings_module_name: name of settings module eg:
         "project.setting"

    Usage:
    >>> from lib import env
    >>> env.setup()
    >>> # from now on paths are setup, and django is configured
    >>> # you can use it in separate "sandbox" script just to check
    >>> # things really quick
    """
    from django.utils.importlib import import_module
    from django.core.management import setup_environ
    
    settings_module_name = settings_module_name or 'settings'

    # 1) try to import module
    settings = import_module(settings_module_name)

    # 2) update sys.path
    if root is not None:
        sys.path[0] = os.path.join(root, 'lib')

    # 3) cofigure django
    setup_environ(settings)


# You can use this module as
# WSGIScriptAlias / "path/to/env.py"
def application(environ, start_response):
    setup()
    from django.core.handlers.wsgi import WSGIHandler
    return WSGIHandler()(environ, start_response)

