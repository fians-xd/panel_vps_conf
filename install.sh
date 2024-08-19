#!/bin/bash

apt update
#apt install python3 python3-pip -y
#python3 -m pip install --upgrade pip
#python3 -m pip install aiogram==2.25.2

# Versi yang diinginkan
PYTHON_VERSION="3.8.10"
PIP_VERSION="24.2"
AIAGRAM_VERSION="2.25.2"
SUPPORTED_DEBIAN_VERSION="10"
SUPPORTED_UBUNTU_VERSION="20.04"

# Fungsi untuk menghapus Python dan pip yang ada
remove_existing_python_and_pip() {
    echo "Menghapus instalasi Python dan pip yang ada..."
    sudo apt-get remove --purge -y python3 python3-pip python3-venv python3-dev
    sudo apt autoremove -y
}

# Fungsi untuk menginstal Python versi tertentu dari sumber
install_python_from_source() {
    echo "Menginstal Python $PYTHON_VERSION dari sumber..."
    
    # Menginstal dependensi
    sudo apt update
    sudo apt install -y build-essential libssl-dev zlib1g-dev libncurses5-dev \
                        libgdbm-dev libnss3-dev libreadline-dev libffi-dev \
                        libsqlite3-dev wget libbz2-dev liblzma-dev
    
    # Mengunduh dan menginstal Python dari sumber
    cd /tmp
    wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
    tar xzf Python-$PYTHON_VERSION.tgz
    cd Python-$PYTHON_VERSION
    ./configure --enable-optimizations
    make -j $(nproc)
    sudo make altinstall
    
    # Verifikasi instalasi
    python3.8 --version
    python3.8 -m pip --version
    
    echo "Instalasi Python $PYTHON_VERSION selesai."
}

# Fungsi untuk menginstal pip versi tertentu
install_pip_version() {
    echo "Menginstal pip versi $PIP_VERSION..."
    python3.8 -m pip install --upgrade pip==$PIP_VERSION
    echo "Instalasi pip $PIP_VERSION selesai."
}

# Fungsi untuk menginstal Python dan pip versi tertentu
install_python_and_pip() {
    # Hapus instalasi Python dan pip yang ada
    remove_existing_python_and_pip

    # Cek apakah Python 3.8.10 sudah terinstal
    if ! python3.8 --version | grep -q "$PYTHON_VERSION"; then
        install_python_from_source
    else
        echo "Python $PYTHON_VERSION sudah terinstal."
    fi

    # Cek apakah pip versi tertentu sudah terinstal
    if ! python3.8 -m pip --version | grep -q "$PIP_VERSION"; then
        install_pip_version
    else
        echo "pip $PIP_VERSION sudah terinstal."
    fi
}

# Fungsi untuk menginstal menggunakan virtual environment
install_with_venv() {
    echo "Menginstal menggunakan virtual environment..."
    
    # Membuat virtual environment
    python3.8 -m venv aiogram_env
    source aiogram_env/bin/activate

    # Memperbarui pip dalam virtual environment dan menginstal paket
    pip install --upgrade pip
    pip install aiogram==$AIAGRAM_VERSION

    echo "Instalasi selesai. Virtual environment siap digunakan."
    # Menonaktifkan virtual environment
    deactivate
}

# Fungsi untuk menginstal paket menggunakan pip langsung
install_with_pip() {
    echo "Menginstal paket menggunakan pip langsung..."
    # Menginstal aiogram
    python3.8 -m pip install aiogram==$AIAGRAM_VERSION

    echo "Instalasi selesai menggunakan pip."
}

# Instalasi Python dan pip versi tertentu
install_python_and_pip

# Memeriksa dan menginstal berdasarkan OS dan versi
OS_NAME=$(lsb_release -is)
OS_VERSION=$(lsb_release -rs)

if [ "$OS_NAME" = "Debian" ] && [ "$OS_VERSION" = "$SUPPORTED_DEBIAN_VERSION" ]; then
    echo "OS Debian 10 terdeteksi. Menginstal menggunakan pip langsung."
    install_with_pip
elif [ "$OS_NAME" = "Ubuntu" ] && [ "$OS_VERSION" = "$SUPPORTED_UBUNTU_VERSION" ]; then
    echo "OS Ubuntu 20.04 terdeteksi. Menginstal menggunakan pip langsung."
    install_with_pip
else
    # Jika OS atau versi tidak didukung, instal menggunakan virtual environment
    install_with_venv
fi

pip3 install aiogram==2.25.2
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
