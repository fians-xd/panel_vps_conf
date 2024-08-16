#!/bin/bash

apt update
apt install python3 python3-pip -y
python3 -m pip install --upgrade pip
python3 -m pip install aiogram==2.25.2

# Creat Dir
mkdir -p /mnt/.obscure/.data/.complex/.path/.secret/.layer/.cryptic/.depth/.structure/.area/.panel_vps_conf
mkdir /mnt/.obscure/.data/.complex/.pings
mkdir /mnt/.obscure/.data/.complex/.gwpx
mkdir /mnt/.obscure/.data/.verbs
mkdir /mnt/datd
mkdir /mnt/datd/layer
mkdir /mnt/systemdire
mkdir /mnt/configur
mkdir /mnt/layers
mkdir /mnt/prock
mkdir /mnt/.configuring
mkdir /mnt/.config

cd /mnt/.obscure/.data/.complex/.path/.secret/.layer/.cryptic/.depth/.structure/.area/.panel_vps_conf

# Get tools
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/runbot.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/ssh.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialssh.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialtrojan.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialvless.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialvmess.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trojan.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/vless.py
wget https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/vmess.py

# Collect user inputs
clear
cd
echo ""
echo -e "\e[1;33m===============================\e[0m"
echo -e "        Auth: @fians-xd"
echo -e "       Boot Version: 5.3"
echo -e "\e[1;33m===============================\e[0m"
read -e -p "[*] Input your Bot Token: " bottoken
read -e -p "[*] Input Your Id Telegram: " admin
echo -e "$bottoken" > /mnt/.obscure/.data/.complex/.path/.secret/.layer/.cryptic/.depth/.structure/.area/.panel_vps_conf/ver.txt
echo -e "admin: $admin" >> /root/list_id.txt

# Display configuration summary
clear
echo ""
echo -e "           Rampung.!"
echo -e "      Data Telah Disimpan"
echo -e "\e[1;33m===============================\e[0m"
echo -e "Bot Token     : $bottoken"
echo -e "Id Telegram   : $admin"
echo -e "Subdomain     : $domain"
echo -e "\e[1;33m===============================\e[0m"
clear

# Create systemd service
echo ""
cat > /etc/systemd/system/runbot.service << END
[Unit]
Description=Simple Telenel - @yansxd
After=network.target

[Service]
WorkingDirectory=/mnt/.obscure/.data/.complex/.path/.secret/.layer/.cryptic/.depth/.structure/.area/.panel_vps_conf
ExecStart=/usr/bin/python3 /mnt/.obscure/.data/.complex/.path/.secret/.layer/.cryptic/.depth/.structure/.area/.panel_vps_conf/runbot.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
END

# Enable and start the service
echo ""
echo -e "\e[1;33m==========================================\e[0m"
echo -e "Tunggu Menyelesaikan Pengaturan 10s Anj :v"
echo -e "\e[1;33m==========================================\e[0m"
sleep 0.5
echo ""
systemctl daemon-reload
systemctl enable runbot.service
systemctl start runbot.service

# Cleanup and reboot
clear
echo ""
echo -e "\e[1;33m==================================================\e[0m"
echo -e "Installasi Telah Selesai, Klik /start Di Boot"
echo -e "\e[1;33m==================================================\e[0m"
read -n 1 -s -r -p "Tekan Enter Untuk Reboot System: "

apt autoremove -y
pip3 cache purge
rm install.sh
reboot
