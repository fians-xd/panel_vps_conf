#!/bin/bash

apt update
apt install python3-pip python3-pil -y
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade idna aiogram
git clone https://github.com/fians-xd/panel_vps_conf.git
cd panel_vps_conf
rm ver.txt
cd

# Collect user inputs
clear
echo ""
echo -e "\e[1;33m===============================\e[0m"
echo -e "        Auth: @fians-xd"
echo -e "       Boot Version: 1.0"
echo -e "\e[1;33m===============================\e[0m"
read -e -p "[*] Input your Bot Token: " bottoken
read -e -p "[*] Input Your Id Telegram: " admin
read -e -p "[*] Input Your Subdomain: " domain
echo -e "$bottoken" > /root/panel_vps_conf/ver.txt
echo -e "$admin" >> /root/panel_vps_conf/ver.txt
echo -e "$domain" >> /root/panel_vps_conf/ver.txt

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
WorkingDirectory=/root/panel_vps_conf
ExecStart=/usr/bin/python3 /root/panel_vps_conf/runbot.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
END

# Enable and start the service
echo ""
echo -e "\e[1;33m=======================================\e[0m"
echo -e "Tunggu Menyelesaikan Pengaturan 10s Anj :v"
echo -e "\e[1;33m=======================================\e[0m"
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
cd panel_vps_conf
rm install.sh
rm README.md
rm -rf .git
cd ..
reboot
