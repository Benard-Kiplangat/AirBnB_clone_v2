#!/usr/bin/env python3
# Fabric script that packs the contents of web static into .tgz archive
from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """A function that generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(file_name))

        return file_name
    except:
        return None
