#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""

from fabric.api import env, put, run, local
from os.path import exists

env.hosts = ['107.23.119.223', '54.89.118.36']
env.user = 'ubuntu'  # Replace with your SSH username


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    put(archive_path, '/tmp/')

    file_name = archive_path.split('/')[-1]
    folder_name = file_name.split('.')[0]
    run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(file_name, folder_name))

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(file_name))

    # Move contents of web_static folder to the release folder
    run('mv /data/web_static/releases/{}/web_static/* '
        '/data/web_static/releases/{}/'.format(folder_name, folder_name))

    # Remove unnecessary web_static folder
    run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))

    # Remove symbolic link /data/web_static/current
    run('rm -rf /data/web_static/current')

    # Create a new symbolic link /data/web_static/current
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(folder_name))

    print('New version deployed!')

    return True


if __name__ == "__main__":
    import sys
    do_deploy(sys.argv[2])
