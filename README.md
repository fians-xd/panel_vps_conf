# Panel Config Install
```
apt-get update && apt-get install wget -y && wget --progress=bar:force https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/install.sh 2>&1 | tee /tmp/wget.log | grep --line-buffered -E "HTTP request sent|Length|Saving to|install.sh\s+100%|saved \[" && chmod +x install.sh && ./install.sh
```
