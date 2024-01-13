#!/usr/bin/python3
# Fabric script that packs the contents of web static into .tgz archive
from fabric.api import *
from os.path import exists
env.hosts = ["54.237.52.24", "100.26.252.108"]

def do_deploy(archive_path):
    """A function that deploys a tgz archive to the servers"""
    filename = archive_path.split("/")[-1]
    filena = filename.split(".")[0]
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(filena))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, filena))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(filena, filena))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filena))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(filena))
        return True
    except:
        return False
