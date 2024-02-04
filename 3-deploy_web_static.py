#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers
"""

from fabric.api import env, local, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['107.23.119.223', '54.89.118.36']
env.user = 'ubuntu'

def do_pack():
    """
    Compresses the web_static folder
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Deploys the archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive
        put(archive_path, "/tmp/")
        # Extract the archive
        release_path = "/data/web_static/releases/{}".format(
            archive_path.split('/')[1].split('.')[0]
        )
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(
            archive_path.split('/')[1], release_path))
        # Move files and clean up
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm /tmp/{}".format(archive_path.split('/')[1]))
        # Update the symbolic link
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True
    except Exception as e:
        return False

def deploy():
    """
    Calls do_pack and do_deploy functions
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

if __name__ == "__main__":
    deploy()
