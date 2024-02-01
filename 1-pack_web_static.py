#!/usr/bin/python3
""" archive the web static folder """


from fabric import task
from datetime import datetime
import os

WEB_STATIC_PATH = './web_static'
VERSIONS_PATH = 'versions'


def do_pack():
    if not os.path.exists(VERSIONS_PATH):
        os.makedirs(VERSIONS_PATH)

    timestamp = datetime.now().strftime('%Y%M%D%H%M%S')
    archive_name = 'web_static_{}'.format(timestamp)
    archive_path = os.path.join(VERSIONS_PATH, archive_name)

    tar_command = 'tar -cvzf {} {}'.format(archive_path, WEB_STATIC_PATH)

    local(tar_command)

    if os.path.exists(archive_path):
        print('web_static packed: {} -> {} Bytes'.format(archive_path, os.path.getsize(archive_path)))
        return archive_path
    else:
        print('Failed to create the archive.')
        return None