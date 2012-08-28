# -*- coding: utf-8 -*-

import os
import sys

def create_projectpath(thefile):
    from os.path import join, dirname, abspath
    root = abspath(join(dirname(abspath(thefile)), '..'))
    return lambda *a: join(root, *a)

# "Temporary globals" that migth be useful
# It can be used in each settings file as builtin
projectpath = create_projectpath(__file__)

# sequence of settings module to read
files_base_names = [
    'default',
    'local'
]

for base_name in files_base_names:
    filepath = '%s/%s.py' % (projectpath('settings'), base_name)
    if os.path.exists(filepath):
        execfile(filepath)

# setup pythonpath - add ./lib before any others paths
# overwrite django and other shared python libs
# it's one of 'little ugly hack' that make things works
if os.path.exists(projectpath('lib')) and len(sys.path) > 0 and sys.path[0] is not projectpath('lib'):
    sys.path.insert(0, projectpath('lib'))

# cleanup
del base_name, files_base_names, filepath, projectpath, create_projectpath

