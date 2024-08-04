#!/bin/bash

# Function to install system packages
install_system_packages() {
    apt update && apt upgrade -y
    apt install -y python3 python3-pip git
}

# Function to install Python packages
install_python_packages() {
    # Check if the required Python packages are installed
    pip3 list | grep pillow > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Pillow is not installed. Installing..."
        pip3 install pillow
    else
        echo "Pillow is already installed. Upgrading if necessary..."
        pip3 install --upgrade pillow
    fi

    # Check if requirements file exists and install dependencies
    if [ -f /root/panel_vps_conf/requirements.txt ]; then
        pip3 install -r /root/panel_vps_conf/requirements.txt
    fi
}

# Install system packages
install_system_packages

# Clone repository if not already cloned
if [ ! -d "/root/panel_vps_conf" ]; then
    git clone https://github.com/fians-xd/panel_vps_conf.git
fi

# Install or upgrade Python packages
install_python_packages

# Collect user inputs
echo ""
read -e -p "[*] Input your Bot Token: " bottoken
read -e -p "[*] Input Your Id Telegram: " admin
read -e -p "[*] Input Your Subdomain: " domain
echo -e "$bottoken" > /root/panel_vps_conf/ver.txt
echo -e "$admin" >> /root/panel_vps_conf/ver.txt
echo -e "$domain" >> /root/panel_vps_conf/ver.txt

# Display configuration summary
echo "Done"
echo "Your Data Bot"
echo -e "==============================="
echo "Bot Token     : $bottoken"
echo "Id Telegram   : $admin"
echo "Subdomain     : $domain"
echo -e "==============================="
echo "Setting done Please wait 10s"
sleep 10

# Create systemd service
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
systemctl daemon-reload
systemctl enable runbot.service
systemctl start runbot.service

# Cleanup and reboot
echo -e "==============================================="
echo " Installations complete, type /menu on your bot"
echo -e "==============================================="
read -n 1 -s -r -p "Press any key to Reboot"
rm -rf /root/panel_vps_conf install.sh
reboot
