#!/usr/bin/env bash
# A scripts that sets up our web server for our static content in nginx
sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Hello World!" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -fR ubuntu:ubuntu /data/

sudo printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /data/web_static/current/;
     location /hbnb_static/ {
     			alias /data/web_static/current/;
		}
     index       index.html index.htm;
}
" > /etc/nginx/sites-available/default
