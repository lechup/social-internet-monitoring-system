# -*- coding: utf-8 -*-
from fabric.api import task, run, env
from fabric.context_managers import cd
from time import sleep

####################
## CONFIG
env.project_root = '~/facewithme/'
env.activate_virtual_env = 'source ~/.virtualenvs/facewithme/bin/activate'
env.hosts = ['facewithme@ovh2.irynek.pl:26']
env.roledefs = {
    'web': env.hosts,
}
def virtualenv(command):
    return run(env.activate_virtual_env + ' && ' + command)
## CONFIG
####################

@task
def clear_cache():
    with cd(env.project_root):
        virtualenv(u'python manage.py clear_cache')


@task
def git_pull():
    with cd(env.project_root):
        run(u'git pull')


@task
def collectstatic():
    with cd(env.project_root):
        virtualenv(u'python manage.py collectstatic --noinput')


@task
def restart_server():
    with cd(env.project_root):
        run(u'touch uwsgi.xml')


@task
def deploy():
    git_pull()
    collectstatic()
    restart_server()
#    sleep(4)    
#    clear_cache()
