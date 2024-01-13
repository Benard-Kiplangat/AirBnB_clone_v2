#!/usr/bin/env bash
# A scripts that sets up our web server for our static content in nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     server_name = $HOST_NAME;
     location /hbnb_static/ {
     			alias /data/web_static/current/;
		}
     index       index.html index.htm;
}
" > /etc/nginx/sites-available/default
sudo service nginx start
