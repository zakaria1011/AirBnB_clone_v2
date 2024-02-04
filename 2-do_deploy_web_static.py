#!/usr/bin/python3
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['107.23.119.223', '54.89.118.36']


def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    folder_name = file_name.split('.')[0]

    put(archive_path, '/tmp/{}'.format(file_name))
    run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(file_name, folder_name))
    run('rm /tmp/{}'.format(file_name))
    run('mv /data/web_static/releases/{0}/web_static/* '
        '/data/web_static/releases/{0}/'.format(folder_name))
    run('rm -rf /data/web_static/releases/{}/web_static'
        .format(folder_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ '
        '/data/web_static/current'.format(folder_name))
    print("New version deployed!")
    return True
