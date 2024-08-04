#!/bin/bash

#install
rm -rf install.sh
apt update && apt upgrade
apt install python3 python3-pip git
git clone https://github.com/fians-xd/panel_vps_conf.git
pip3 install pillow
#pip3 install -r panel_vps_conf/requirements.txt

#isi data
echo ""
read -e -p "[*] Input your Bot Token: " bottoken
read -e -p "[*] Input Your Id Telegram: " admin
read -e -p "[*] Input Your Subdomain: " domain
echo -e "$bottoken" >> /root/panel_vps_conf/ver.txt
echo -e "$admin" >> /root/panel_vps_conf/ver.txt
echo -e "$domain" >> /root/panel_vps_conf/ver.txt
#clear
echo "Done"
echo "Your Data Bot"
echo -e "==============================="
echo "Bot Token     : $bottoken"
echo "Id Telegram   : $admin"
echo "Subdomain     : $domain"
echo -e "==============================="
echo "Setting done Please wait 10s"
sleep 10

cat > /etc/systemd/system/runbot.service << END
[Unit]
Description=Simple Telenel - @yansxd
After=network.target

[Service]
WorkingDirectory=/root
ExecStart=/usr/bin/python3 /root/panel_vps_conf/runbot.py
Restart=always

[Install]
WantedBy=multi-user.target
END

systemctl daemon-reload
systemctl enable runbot.service
systemctl start runbot.service


#clear

echo -e "==============================================="
echo " Installations complete, type /menu on your bot"
echo -e "==============================================="
read -n 1 -s -r -p "Press any key to Reboot"
rm -rf panel_vps_conf xolpanel.sh
#clear
#reboot

