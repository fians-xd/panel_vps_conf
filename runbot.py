#!/usr/bin/env python3

import re
import os
import socket
import aiohttp
import logging
import asyncio
import platform
import subprocess
from datetime import datetime
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Membaca token dari file ver.txt
def get_api_token(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

# Path ke file ver.txt
file_path = '/mnt/.obscure/.data/.complex/.path/.secret/.layer/.cryptic/.depth/.structure/.area/.panel_vps_conf/ver.txt'
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

logincek_script_map = {
    'start_ssh_creation': 'cek.py',
    'start_vmess_creation': 'cek-ws.py',
    'start_vless_creation': 'cek-vless.py',
    'start_trojan_creation': 'cek-tr.py'
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
    InlineKeyboardButton("【 Monitor 】", callback_data="monitor"),
    InlineKeyboardButton("【 Reboot 】", callback_data="reboot"),
    InlineKeyboardButton("【 Clear Cache 】", callback_data="clear_cache"),
    InlineKeyboardButton("【 Status Service 】", callback_data="status_service"),
    InlineKeyboardButton("【 Set Autoreboot 】", callback_data="set_autoreboot"),
    InlineKeyboardButton("【 Restart All Service 】", callback_data="reset_all_service")
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

def create_bar(percentage, length=10):
    filled_length = int(length * percentage // 100)
    bar = '|' * filled_length + '-' * (length - filled_length)
    return bar

def is_id_allowed(chat_or_user_id):
    allowed_ids_path = '/root/list_id.txt'
    
    if not os.path.exists(allowed_ids_path):
        logging.error(f"File {allowed_ids_path} tidak ditemukan.")
        return False
    
    allowed_ids = set()
    with open(allowed_ids_path, 'r') as file:
        for line in file:
            # Gunakan regex untuk mencari angka positif dan negatif di dalam baris
            ids_in_line = re.findall(r'-?\d+', line)
            allowed_ids.update(ids_in_line)
    
    return str(chat_or_user_id) in allowed_ids

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    # Cek apakah user_id atau chat_id diperbolehkan
    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
        await message.answer("Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
        return

    # Jalankan script shell untuk memperbarui log
    subprocess.run(['ingpo'], check=True)

    # Baca hasil log
    with open('/etc/ingpo.log', 'r') as log_file:
        log_content = log_file.read()

    # Baca hasil log
    with open('/etc/ingpo-pengguna.log', 'r') as log_pengguna:
        log_pengguna = log_pengguna.read()

    # Kirim pesan dengan isi log
    await message.answer(
        f"➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠\n"
        f" ∧,,,∧  🧑‍💻 𝐀𝐃𝐌𝐈𝐍 𝐏𝐀𝐍𝐄𝐋 𝐒𝐂 🧑‍💻  ^  ִֶָ𖦹\n"
        f"(  ̳• · • ̳)        𝐕𝐞𝐫𝐬𝐢𝐨𝐧 𝐛𝐨𝐭: 𝟓.𝟕   𓂃    ©  \n"
        f"/    づ♡ ♡  𝐀𝐮𝐭𝐡𝐨𝐫: 𝐒𝐨𝐟𝐢𝐚𝐧-𝐍  °  𓂃 ࣪ ˖  ִֶָ𐀔\n"
        f"➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠\n"
        f"{log_content}"
        f"➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠\n"
        f"{log_pengguna}"
        f"➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠\n",
        parse_mode='Markdown',
        reply_markup=main_keyboard
    )
        
@dp.callback_query_handler(lambda c: c.data in protocol_map)
async def handle_protocol(query: types.CallbackQuery):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    
    # Cek apakah user_id atau chat_id diperbolehkan
    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
        await query.message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
        return

    action = protocol_map.get(query.data)
    if action:
        user_data[query.from_user.id] = {'action': action}
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("【 Live Akun 】", callback_data=f'{query.data}_live'),
            InlineKeyboardButton("【 Trial Akun 】", callback_data=f'{query.data}_trial'),
            InlineKeyboardButton("【 Cek User Login Akun 】", callback_data=f'{query.data}_login')
        )
        await query.message.edit_text(text="‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎‎~=【  PILIH TIPE AKUN  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=keyboard)
        await query.answer()
    else:
        await query.answer(text="Invalid protocol key.", show_alert=True)

@dp.callback_query_handler(lambda c: c.data.endswith('_live') or c.data.endswith('_trial') or c.data.endswith('_login'))
async def handle_type(query: types.CallbackQuery):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    
    # Cek apakah user_id atau chat_id diperbolehkan
    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
        await query.message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
        return

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
                        await query.message.edit_text(f"{stdout_str}", parse_mode='Markdown')
                except Exception as e:
                    logging.error(f"Exception occurred while running the script: {str(e)}")
                    await query.message.edit_text(f"Exception occurred while running trial {action.split('_')[1].capitalize()} Account:\n{str(e)}")
            else:
                await query.message.edit_text("Script not found.")

        elif account_type == 'login':
            script = logincek_script_map.get(action)
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
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    
    # Cek apakah user_id atau chat_id diperbolehkan
    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
        await query.message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
        return

    await query.message.edit_reply_markup(reply_markup=None)
    await query.message.edit_text("‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎ ‎‎ ‎ ‎‎~=【  Harap Hati-Hati  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=settings_keyboard)
    await query.answer()

#------------------------------------------------------------------------------------------------------------
async def show_loading_bar(query, task_name):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    
    # Cek apakah user_id atau chat_id diperbolehkan
    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
        await query.message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
        return

    msg = await bot.send_message(query.from_user.id, f"{task_name}: ")
    for i in range(1, 11):
        await msg.edit_text(f"{task_name}: [{create_bar(i * 10)}] {i * 10}%")
        await asyncio.sleep(0.5)
    return msg

async def run_system_command(command):
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode().strip(), stderr.decode().strip(), process.returncode

@dp.callback_query_handler(lambda c: c.data in ['monitor', 'reboot', 'clear_cache', 'reset_all_service', 'set_autoreboot', 'status_service'])
async def process_settings(query: types.CallbackQuery):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    
    # Cek apakah user_id atau chat_id diperbolehkan
    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
        await query.message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
        return

    action = query.data

    # Hilangkan tombol sementara
    await query.message.edit_reply_markup(reply_markup=None)

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
        #await bot.send_message(query.from_user.id, "‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎‎~=【  Harap Hati-Hati  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=settings_keyboard)

    elif action == "reboot":
        await bot.send_message(query.from_user.id, "Get '/start' After 5-10 seconds, Wait for the OS to load.!")
        await asyncio.sleep(5)
        os.system("reboot")

    elif action == "clear_cache":
        loading_msg = await show_loading_bar(query, 'Clear Cache')
        await run_system_command('sync; echo 1 > /proc/sys/vm/drop_caches')
        await loading_msg.edit_text("Cache cleared successfully.!")
        #await bot.send_message(query.from_user.id, "‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎‎~=【  Harap Hati-Hati  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=settings_keyboard)

    elif action == "reset_all_service":
        loading_msg = await show_loading_bar(query, 'Restart All Services')
        cxmd = "asuk"
        await run_system_command(cxmd)
        await loading_msg.edit_text("All services restarted successfully.!")
        #await bot.send_message(query.from_user.id, "‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎‎~=【  Harap Hati-Hati  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=settings_keyboard)

    elif action == "status_service":
        cmd = "running"
        await run_system_command(cmd)
        with open('/etc/status-service.log', 'r') as f:
            log_data = f.read()
        await bot.send_message(query.from_user.id, f"{log_data}")
        #await bot.send_message(query.from_user.id, "‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎‎~=【  Harap Hati-Hati  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=settings_keyboard)

    elif action == "set_autoreboot":
        await bot.send_message(query.from_user.id, "Autoreboot telah di-set 5 jam sekali.!")
        #await bot.send_message(query.from_user.id, "‎‎ \n ‎‎  ‎ ‎‎ ‎  ‎ ‎‎~=【  Harap Hati-Hati  】=~ ‎‎ ‎   ‎ ‎‎ ‎ ‎‎", reply_markup=settings_keyboard)

#---------------------------------------------------------------------------------------------------------------------------------
@dp.message_handler(lambda message: message.from_user.id in user_data and 'action' in user_data[message.from_user.id])
async def handle_input(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    # Cek apakah user_id atau chat_id diperbolehkan
    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
        await message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
        return

    user_id = message.from_user.id
    action = user_data[user_id]['action']
    input_text = message.text

    logging.info(f'Handling input: user_id={user_id}, action={action}, input_text={input_text}')

    if 'username' not in user_data[user_id]:
        # Validate username length
        if len(input_text) < 6:
            await message.reply('Minimal 6 Huruf Njirr.!')
            return
        
        user_data[user_id]['username'] = input_text
        if action == 'start_ssh_creation':
            await message.reply('Masukkan Password Akun SSH:')
        else:
            await message.reply(f'Masukkan Berapa Lama Xpired {action.split("_")[1].capitalize()} contoh (1,2,3 dll):')
        return

    if action == 'start_ssh_creation' and 'password' not in user_data[user_id]:
        # Validate password length and content
        if len(input_text) < 6 or not re.search(r'\d', input_text) and not re.search(r'[^\w\s]', input_text):
            await message.reply('Minimal 6 huruf dan harus ada satu angka atau karakter khusus.')
            return
        
        user_data[user_id]['password'] = input_text
        await message.reply('Masukkan Berapa Lama Xpired SSH contoh (1,2,3 dll):')
        return

    if 'expiry' not in user_data[user_id]:
        # Validate expiry input
        if not input_text.isdigit():
            await message.reply('Input angka jancok.!')
            return
        
        user_data[user_id]['expiry'] = input_text

    username = user_data[user_id].get('username')
    password = user_data[user_id].get('password', '')
    expiry_days = user_data[user_id].get('expiry')
    script = script_map.get(action)

    if script:
        try:
            if action == 'start_ssh_creation':
                    user_id = message.from_user.id
                    chat_id = message.chat.id
    
                    # Cek apakah user_id atau chat_id diperbolehkan
                    if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
                        await message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
                        return
                    args = ['python3', script, username, password, expiry_days]
            else:
                user_id = message.from_user.id
                chat_id = message.chat.id
    
                # Cek apakah user_id atau chat_id diperbolehkan
                if not is_id_allowed(user_id) and not is_id_allowed(chat_id):
                        await message.edit_text(text="Izin dulu cah ganteng 🙃\nJapri: wa.me/6285788962287")
                        return
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
                await message.reply(f"{stdout_str}", parse_mode='Markdown')
        except Exception as e:
            logging.error(f"Exception occurred while running the script: {str(e)}")
            await message.reply(f"Exception occurred while creating {action.split('_')[1].capitalize()} Account:\n{str(e)}")
    else:
        await message.reply("Script not found.")
        return

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
