#!/usr/bin/python3
""" Archive the web static folder """

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ """
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = 'versions/web_static_{}.tgz'.format(timestamp)

    local('tar -cvzf {}'.format(file_path))

    size = os.path.getsize(file_path)
    if os.path.exists(archive_path):
        print('web_static packed: {} -> {} Bytes'.format(file_path, size))
        return file_path
    else:
        print('Failed to create the archive.')
        return None
