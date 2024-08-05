#!/bin/bash

apt update
apt install python3-pip
python3 -m pip install --upgrade pip
pip3 install --upgrade idna
apt install python3-pil
git clone https://github.com/fians-xd/panel_vps_conf.git
apt install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev
pip3 install python-telegram-bot setuptools wheel telegram
pip3 cache purge

# Collect user inputs
clear
echo ""
echo -e "==============================="
echo "        Auth: @fians-xd"
echo "       Boot Version: 1.0"
echo -e "==============================="
read -e -p "[*] Input your Bot Token: " bottoken
read -e -p "[*] Input Your Id Telegram: " admin
read -e -p "[*] Input Your Subdomain: " domain
echo -e "$bottoken" > /root/panel_vps_conf/ver.txt
echo -e "$admin" >> /root/panel_vps_conf/ver.txt
echo -e "$domain" >> /root/panel_vps_conf/ver.txt

# Display configuration summary
clear
echo ""
echo "           Rampung.!"
echo "      Data Telah Disimpan"
echo -e "==============================="
echo "Bot Token     : $bottoken"
echo "Id Telegram   : $admin"
echo "Subdomain     : $domain"
echo -e "==============================="
echo "Setting done Please wait 10s"
sleep 10

# Create systemd service
echo ""
cat > /etc/systemd/system/runbot.service << END
[Unit]
Description=Simple Telenel - @yansxd
After=network.target

[Service]
WorkingDirectory=/root/panel_vps_conf
ExecStart=/usr/bin/python3 /root/panel_vps_conf/runbot.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
END

# Enable and start the service
echo ""
systemctl daemon-reload
systemctl enable runbot.service
systemctl start runbot.service

# Cleanup and reboot
echo ""
echo -e "==============================================="
echo " Installations complete, type /menu on your bot"
echo -e "==============================================="
read -n 1 -s -r -p "Press any key to Reboot"
rm panel_vps_conf/install.sh
reboot
