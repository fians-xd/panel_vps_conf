#!/bin/bash

rm install.sh
apt-get update
apt-get install python3 python3-pip -y
python3 -m pip install --upgrade pip
python3 -m pip install psutil aiogram==2.25.2

# Warna
biru="\e[36m"
red="\e[1;31m"
green="\e[0;32m"
yell="\e[1;33m"
tyblue="\e[1;36m"
BRed="\e[1;31m"
BGreen="\e[1;32m"
BGren="\e[1;44m"
BYellow="\e[1;33m"
BBlue="\e[1;34m"
NC="\e[0m"

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
clear
echo " "
# Spinner function
spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " \r${biru}~=[ ${green}Please Wait, the System is Being Configured.. %c ${biru}]=~${NC}" "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
    done
}

# Proses wget dengan spinner
(
  # Get tools
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/runbot.py

  # Creat Account Live
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/ssh.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trojan.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/vless.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/vmess.py

  # Creat Account Trial
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialssh.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialtrojan.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialvless.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialvmess.py

  # Cek Login Account
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek-vless.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek-tr.py
  wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek-ws.py
) & spinner

#echo -e "${biru} ~=[ ${green}Please Wait, the System is Being Configured..! ${biru}]=~${NC}"
#echo " "

# Get tools
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/runbot.py

# Creat Account Live
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/ssh.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trojan.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/vless.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/vmess.py

# Creat Account Trial
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialssh.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialtrojan.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialvless.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/trialvmess.py

# Cek Login Account
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek-vless.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek-tr.py
#wget -q https://raw.githubusercontent.com/fians-xd/panel_vps_conf/master/cek-ws.py

# Collect user inputs
clear
cd
echo ""
echo -e "\e[1;33m===============================\e[0m"
echo -e "        Auth: @fians-xd"
echo -e "       Boot Version: 5.7"
echo -e "\e[1;33m===============================\e[0m"
read -e -p "[*] Input Bot Token: " bottoken
read -e -p "[*] Input Id Telegram: " admin
echo -e "$bottoken" > /mnt/.obscure/.data/.complex/.path/.secret/.layer/.cryptic/.depth/.structure/.area/.panel_vps_conf/ver.txt
echo -e "admin: $admin" >> /root/list_id.txt

# Display configuration summary
clear
echo ""
echo -e "\e[1;33m===============================\e[0m"
echo -e "            Rampung.!"
echo -e "       Data Telah Disimpan"
echo -e "\e[1;33m===============================\e[0m"
echo -e " Bot Token     : $bottoken"
echo -e " Id Telegram   : $admin"
echo -e "\e[1;33m===============================\e[0m"
sleep 0.7
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
echo -e "\e[1;33m==================================================\e[0m"
echo -e "  Tunggu Menyelesaikan Pengaturan 10s Anj :v"
echo -e "\e[1;33m==================================================\e[0m"
sleep 0.5
echo ""
systemctl daemon-reload
systemctl enable runbot.service
systemctl start runbot.service

# Cleanup and reboot
clear
echo ""
echo -e "\e[1;33m==================================================\e[0m"
echo -e "  Installasi Telah Selesai, Klik /start Di Boot"
echo -e "\e[1;33m==================================================\e[0m"
read -n 1 -s -r -p "Tekan Enter Untuk Reboot System: "

apt-get autoremove -y
pip cache purge
pip3 cache purge
