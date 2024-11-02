#!/bin/bash

# CHEK STATUS
tls_v2ray_status=$(systemctl status xray | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
nontls_v2ray_status=$(systemctl status xray | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
vless_tls_v2ray_status=$(systemctl status xray | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
vless_nontls_v2ray_status=$(systemctl status xray | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
shadowsocks=$(systemctl status xray | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
trojan_server=$(systemctl status xray | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
dropbear_status=$(/etc/init.d/dropbear status | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
stunnel_service=$(/etc/init.d/stunnel4 status | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
ssh_service=$(/etc/init.d/ssh status | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
vnstat_service=$(/etc/init.d/vnstat status | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
cron_service=$(/etc/init.d/cron status | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
fail2ban_service=$(/etc/init.d/fail2ban status | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
wstls=$(systemctl status ws-stunnel.service | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
wsdrop=$(systemctl status ws-dropbear.service | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
udp=$(systemctl status udp-custom | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
nginx_service=$(/etc/init.d/nginx status | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)
ovpn=$(systemctl status openvpn | grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1)

# STATUS SERVICE OpenVpn
if [[ $ovpn == "exited" || $ovpn == "running" ]]; then
   openvpn_tele=" Running ✅"
else
   openvpn_tele=" Running ❌"
fi

# STATUS SERVICE  VNSTAT 
if [[ $vnstat_service == "running" ]]; then 
   status_vnstat_tele=" Running ✅"
else
   status_vnstat_tele=" Running ❌"
fi

# STATUS SERVICE  CRONS 
if [[ $cron_service == "running" ]]; then
   status_cron_tele=" Running ✅"
else
   status_cron_tele=" Running ❌"
fi

# STATUS SERVICE  SSH 
if [[ $ssh_service == "running" ]]; then
   status_ssh_tele=" Running ✅"
else
   status_ssh_tele=" Running ❌"
fi

# STATUS SERVICE SQUID 
if [[ $squid_service == "running" ]]; then 
   status_squid_tele=" Running ✅"
else
   status_squid_tele=" Running ❌"
fi

# STATUS SERVICE FAIL2BAN 
if [[ $fail2ban_service == "running" ]]; then
   status_fail2ban_tele=" Running ✅"
else
   status_fail2ban_tele=" Running ❌"
fi

# STATUS SERVICE TLS 
if [[ $tls_v2ray_status == "running" ]]; then
   status_tls_v2ray_tele=" Running ✅"
else
   status_tls_v2ray_tele=" Running ❌"
fi

# STATUS SERVICE NON TLS V2RAY
if [[ $nontls_v2ray_status == "running" ]]; then
   status_nontls_v2ray_tele=" Running ✅"
else
   status_nontls_v2ray_tele=" Running ❌"
fi

# STATUS SERVICE VLESS HTTPS
if [[ $vless_tls_v2ray_status == "running" ]]; then
  status_tls_vless_tele=" Running ✅"
else
  status_tls_vless_tele=" Running ❌"
fi

# STATUS SERVICE VLESS HTTP
if [[ $vless_nontls_v2ray_status == "running" ]]; then
  status_nontls_vless_tele=" Running ✅"
else
  status_nontls_vless_tele=" Running ❌"
fi

# STATUS SERVICE TROJAN
if [[ $trojan_server == "running" ]]; then
   status_trojan_tele=" Running ✅"
else
   status_trojan_tele=" Running ❌"
fi

# STATUS SERVICE DROPBEAR
if [[ $dropbear_status == "running" ]]; then
   status_beruangjatuh_tele=" Running ✅"
else
   status_beruangjatuh_tele=" Running ❌"
fi

# STATUS SERVICE STUNNEL
if [[ $stunnel_service == "running" ]]; then
   status_stunnel_tele=" Running ✅"
else
   status_stunnel_tele=" Running ❌"
fi

# STATUS SERVICE WEBSOCKET TLS
if [[ $wstls == "running" ]]; then
   swstls_tele=" Running ✅"
else
   swstls_tele=" Running ❌"
fi

# STATUS SERVICE WEBSOCKET DROPBEAR
if [[ $wsdrop == "running" ]]; then
   status_swsdrop_tele=" Running ✅"
else
   status_swsdrop_tele=" Running ❌"
fi

# STATUS SHADOWSOCKS
if [[ $shadowsocks == "running" ]]; then
   status_shadowsocks_tele=" Running ✅"
else
   status_shadowsocks_tele=" Running ❌"
fi

# STATUS UDP-CUSTOM
if [[ $udp == "running" ]]; then
   status_udp_tele=" Running ✅"
else
   status_udp_tele=" Running ❌"
fi

# STATUS NGINX
if [[ $nginx_service == "running" ]]; then
   status_nginx_tele=" Running ✅"
else
   status_nginx_tele=" Running ❌"
fi

# Ini Output Untuk Pesan Bot Telegram Tanpa kode warna ansi
{
   echo "━━━━━━━━━━━━━━━━━━━━━━"
   echo "          SERVICE INFORMATION           "
   echo "━━━━━━━━━━━━━━━━━━━━━━"
   echo "Cron 👉 $status_cron_tele"
   echo "Nginx 👉 $status_nginx_tele"
   echo "Stunl4 👉 $status_stunnel_tele"
   echo "Ws-tls 👉 $swstls_tele"
   echo "Trojan 👉 $status_trojan_tele"
   echo "Vnstat 👉 $status_vnstat_tele"
   echo "Fl2-ban 👉 $status_fail2ban_tele"
   echo "Vles-tls 👉 $status_tls_vless_tele"
   echo "Ws-n.tls 👉 $swstls_tele"
   echo "OpenVpn👉 $openvpn_tele"
   echo "Ssh/Tun 👉 $status_ssh_tele"
   echo "Vmes-tls 👉 $status_tls_v2ray_tele"
   echo "Vles-n.tls 👉 $status_nontls_vless_tele"
   echo "Dropbear 👉 $status_beruangjatuh_tele"   
   echo "Vmes-n.tls 👉 $status_nontls_v2ray_tele"
   echo "Shw-socks 👉 $status_shadowsocks_tele"
   echo "Udp-Custom 👉 $status_udp_tele"
   echo "━━━━━━━━━━━━━━━━━━━━━━"
   echo ""
} | sed -e 's/\x1b\[[0-9;]*m//g' > /etc/status-service.log
