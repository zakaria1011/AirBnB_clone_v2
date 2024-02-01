#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path import isdir
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file = "versions/web_static_{}.tgz".format(timestamp)
    if isdir("versions") is False:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file))
        return file
    else:
    return file