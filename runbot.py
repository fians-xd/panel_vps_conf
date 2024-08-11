from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import subprocess
import logging
import os
import asyncio

# Membaca token dari file ver.txt
def get_api_token(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

# Path ke file ver.txt
file_path = 'ver.txt'
API_TOKEN = get_api_token(file_path)

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Membuat instance bot dan dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

user_data = {}

protocol_map = {
    'buat_ssh': 'start_ssh_creation',
    'buat_vmess': 'start_vmess_creation',
    'buat_vless': 'start_vless_creation',
    'buat_trojan': 'start_trojan_creation'
}

script_map = {
    'start_ssh_creation': 'ssh.py',
    'start_vmess_creation': 'vmess.py',
    'start_vless_creation': 'vless.py',
    'start_trojan_creation': 'trojan.py'
}

trial_script_map = {
    'start_ssh_creation': 'trialssh.py',
    'start_vmess_creation': 'trialvmess.py',
    'start_vless_creation': 'trialvless.py',
    'start_trojan_creation': 'trialtrojan.py'
}

prompt_map = {
    'start_ssh_creation': 'Masukkan Nama Akun SSH:',
    'start_vmess_creation': 'Masukkan Nama Akun VMess:',
    'start_vless_creation': 'Masukkan Nama Akun VLess:',
    'start_trojan_creation': 'Masukkan Nama Akun Trojan:',
    'fitur_ini_belum_tersedia': 'Fitur ini Belum tersedia..!!'
}

# Keyboard utama dengan tombol pengaturan
main_keyboard = InlineKeyboardMarkup(row_width=2)
main_keyboard.add(
    InlineKeyboardButton("【 SSH 】", callback_data='buat_ssh'),
    InlineKeyboardButton("【 Vmess 】", callback_data='buat_vmess')
)
main_keyboard.add(
    InlineKeyboardButton("【 Vless 】", callback_data='buat_vless'),
    InlineKeyboardButton("【 Trojan 】", callback_data='buat_trojan')
)
main_keyboard.add(
    InlineKeyboardButton("【 Your OS Settings 】", callback_data='settings')
)
main_keyboard.add(
    InlineKeyboardButton("【 Donate 】", url='wa.me/6285788962287'),
    InlineKeyboardButton("【 Serv fees 】", url='https://t.me/+LTtQ920p7PBhNTRl')
)
main_keyboard.add(
    InlineKeyboardButton("【 Report Bug To Mee Auth 】", url='t.me/yansxdi')
)

# Keyboard pengaturan
settings_keyboard = InlineKeyboardMarkup(row_width=2)
settings_buttons = [
    InlineKeyboardButton("Monitor", callback_data="monitor"),
    InlineKeyboardButton("Reboot", callback_data="reboot"),
    InlineKeyboardButton("Clear Cache", callback_data="clear_cache"),
    InlineKeyboardButton("Status Service", callback_data="status_service"),
    InlineKeyboardButton("Set Autoreboot", callback_data="set_autoreboot"),
    InlineKeyboardButton("Restart All Service", callback_data="reset_all_service")
]
settings_keyboard.add(*settings_buttons)

def get_cpu_usage():
    with open('/proc/stat', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if 'cpu ' in line:
            data = line.split()
            total = sum(map(int, data[1:]))
            idle = int(data[4])
            usage = (total - idle) / total * 100
            return usage

def create_bar(percentage, length=10):  # Bar length shortened for a more compact display
    filled_length = int(length * percentage // 100)
    bar = '|' * filled_length + '-' * (length - filled_length)
    return bar

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "==============================\n"
        " ∧,,,∧  🧑‍💻 ADMIN PANEL SC 🧑‍💻  ^  ִֶָ𖦹\n"
        "(  ̳• · • ̳)        Version bot: 4.5   𓂃    ©  \n"
        "/    づ♡ ♡  Author: Sofian-n  °  𓂃 ࣪ ˖  ִֶָ𐀔\n"
        "==============================\n",
        parse_mode='Markdown',
        reply_markup=main_keyboard
    )

@dp.callback_query_handler(lambda c: c.data in protocol_map)
async def handle_protocol(query: types.CallbackQuery):
    action = protocol_map.get(query.data)
    if action:
        user_data[query.from_user.id] = {'action': action}
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("【 Live Akun 】", callback_data=f'{query.data}_live'),
            InlineKeyboardButton("【 Trial Akun 】", callback_data=f'{query.data}_trial')
        )
        await query.message.edit_text(text="‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎‎~=【  PILIH TIPE AKUN  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=keyboard)
        await query.answer()
    else:
        await query.answer(text="Invalid protocol key.", show_alert=True)

@dp.callback_query_handler(lambda c: c.data.endswith('_live') or c.data.endswith('_trial'))
async def handle_type(query: types.CallbackQuery):
    protocol_key, account_type = query.data.rsplit('_', 1)
    action = protocol_map.get(protocol_key)

    logging.info(f'Handling type: protocol_key={protocol_key}, account_type={account_type}, action={action}')

    if action:
        user_data[query.from_user.id]['type'] = account_type
        if account_type == 'live':
            await query.message.edit_text(text=prompt_map.get(action, 'Action not implemented.'))
        elif account_type == 'trial':
            script = trial_script_map.get(action)
            if script:
                try:
                    process = subprocess.Popen(['python3', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    stdout_str = stdout.decode().strip()
                    stderr_str = stderr.decode().strip()

                    logging.info(f"Process output: {stdout_str}")
                    if process.returncode != 0 or stderr_str:
                        logging.error(f"Process error: {stderr_str}")
                        await query.message.edit_text(f"Error while running trial {action.split('_')[1].capitalize()} Account:\n{stderr_str}")
                    else:
                        await query.message.edit_text(f"{stdout_str}")
                except Exception as e:
                    logging.error(f"Exception occurred while running the script: {str(e)}")
                    await query.message.edit_text(f"Exception occurred while running trial {action.split('_')[1].capitalize()} Account:\n{str(e)}")
            else:
                await query.message.edit_text("Script not found.")
        await query.answer()
    else:
        await query.answer(text="Invalid protocol key.", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'settings')
async def show_settings(query: types.CallbackQuery):
    await query.message.edit_text("Harap Hati-Hati:", reply_markup=settings_keyboard)
    await query.answer()

@dp.callback_query_handler(lambda c: c.data in ['monitor', 'reboot', 'clear_cache', 'reset_all_service', 'set_autoreboot', 'status_service'])
async def process_settings(query: types.CallbackQuery):
    action = query.data

    if action == "monitor":
        cpu_usage = get_cpu_usage()
        memory_usage = os.popen("free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'").readline().strip()
        swap_usage = os.popen("free -m | awk 'NR==3{printf \"%.2f\", $3*100/$2 }'").readline().strip()

        cpu_bar = create_bar(float(cpu_usage))
        memory_bar = create_bar(float(memory_usage))
        swap_bar = create_bar(float(swap_usage))

        await bot.send_message(query.from_user.id,
                               f"CPU Usage: {cpu_bar} {cpu_usage:.2f}%\n"                               
                               f"Swap Usage: {swap_bar} {swap_usage}%\n"
                               f"Memory Usage: {memory_bar} {memory_usage}%")

    elif action == "reboot":
        await bot.send_message(query.from_user.id, "Ketik '/start' lagi setelah 5-10 detik, menunggu OS dimuat.!")
        await asyncio.sleep(5)
        os.system("reboot")

    elif action == "clear_cache":
        os.system("apt-get autoremove -y && apt-get autoclean -y")
        await bot.send_message(query.from_user.id, "Selesai membersihkan sampah.!")

    elif action == "set_autoreboot":
        os.system("(crontab -l ; echo '0 0 * * * /sbin/reboot') | crontab -")
        await bot.send_message(query.from_user.id, "VPS ini akan reboot otomatis setiap 24 jam sekali.")

    elif action == "reset_all_service":
        await bot.send_message(query.from_user.id, "Mereset semua layanan, mohon tunggu...")
        
        services = [
            '/etc/init.d/ssh restart',
            '/etc/init.d/dropbear restart',
            '/etc/init.d/stunnel4 restart',
            '/etc/init.d/openvpn restart',
            '/etc/init.d/fail2ban restart',
            '/etc/init.d/cron restart',
            '/etc/init.d/nginx restart',
            '/etc/init.d/squid restart',
            'systemctl restart xray',
            'systemctl restart sshws.service',
            'systemctl restart ws-dropbear.service',
            'systemctl restart ws-stunnel.service',
            'systemctl restart trojan-go.service',
            'screen -dmS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7100 --max-clients 500',
            'screen -dmS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7200 --max-clients 500',
            'screen -dmS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7300 --max-clients 500'
        ]

        for service in services:
            process = subprocess.run(service, shell=True, capture_output=True, text=True)
            if process.returncode != 0:
                logging.error(f"Error while restarting service '{service}': {process.stderr.strip()}")
        
        await bot.send_message(query.from_user.id, "Semua layanan telah di restart.!")

    elif action == "status_service":
        await bot.send_message(query.from_user.id, "Memindai status layanan...")
        try:
            # Jalankan skrip shell 'running'
            subprocess.run('running', shell=True, check=True)
        
            # Baca hasil output dari file log
            with open('/etc/status-service.log', 'r') as file:
                status_log = file.read()
                
            await bot.send_message(query.from_user.id, f"{status_log}")

        except subprocess.CalledProcessError as e:
            logging.error(f"Error while running the script: {e.stderr.strip()}")
            await bot.send_message(query.from_user.id, "Terjadi kesalahan saat menjalankan skrip status layanan.")

        except FileNotFoundError:
            await bot.send_message(query.from_user.id, "File log status layanan tidak ditemukan.")

        except Exception as e:
            logging.error(f"Exception occurred: {str(e)}")
            await bot.send_message(query.from_user.id, f"Terjadi kesalahan: {str(e)}")

    await query.answer()

@dp.message_handler(lambda message: message.from_user.id in user_data and 'action' in user_data[message.from_user.id])
async def handle_input(message: types.Message):
    user_id = message.from_user.id
    action = user_data[user_id]['action']
    input_text = message.text

    logging.info(f'Handling input: user_id={user_id}, action={action}, input_text={input_text}')

    if 'username' not in user_data[user_id]:
        user_data[user_id]['username'] = input_text
        if action == 'start_ssh_creation':
            await message.reply('Masukkan Password Akun SSH:')
        else:
            await message.reply(f'Masukkan Berapa Lama Xpired {action.split("_")[1].capitalize()} contoh (1,2,3 dll):')
        return

    if action == 'start_ssh_creation' and 'password' not in user_data[user_id]:
        user_data[user_id]['password'] = input_text
        await message.reply('Masukkan Berapa Lama Xpired SSH contoh (1,2,3 dll):')
        return

    if 'expiry' not in user_data[user_id]:
        user_data[user_id]['expiry'] = input_text

    username = user_data[user_id].get('username')
    password = user_data[user_id].get('password', '')
    expiry_days = user_data[user_id].get('expiry')
    script = script_map.get(action)

    if script:
        try:
            if action == 'start_ssh_creation':
                args = ['python3', script, username, password, expiry_days]
            else:
                args = ['python3', script, username, expiry_days]
                
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            stdout_str = stdout.decode().strip()
            stderr_str = stderr.decode().strip()

            logging.info(f"Process output: {stdout_str}")
            if process.returncode != 0 or stderr_str:
                logging.error(f"Process error: {stderr_str}")
                await message.reply(f"Error while creating {action.split('_')[1].capitalize()} Account:\n{stderr_str}")
            else:
                await message.reply(f"{stdout_str}")
        except Exception as e:
            logging.error(f"Exception occurred while running the script: {str(e)}")
            await message.reply(f"Exception occurred while creating {action.split('_')[1].capitalize()} Account:\n{str(e)}")
    else:
        await message.reply("Script not found.")
        return

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
