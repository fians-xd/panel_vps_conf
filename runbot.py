from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import subprocess
import logging

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

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("【 SSH 】", callback_data='buat_ssh'),
        InlineKeyboardButton("【 Vmess 】", callback_data='buat_vmess'),
        InlineKeyboardButton("【 Vless 】", callback_data='buat_vless'),
        InlineKeyboardButton("【 Trojan 】", callback_data='buat_trojan'),
        InlineKeyboardButton("【 Donate 】", url='wa.me/6285788962287'),
        InlineKeyboardButton("【 Server fees 】", url='https://t.me/+LTtQ920p7PBhNTRl'),
        InlineKeyboardButton("【 Report Bug To Me 】", url='t.me/yansxdi')
    )
    await message.answer(
        "==============================\n"
        " ∧,,,∧  🧑‍💻 ADMIN PANEL SC 🧑‍💻  ^  ִֶָ𖦹\n"
        "(  ̳• · • ̳)        Version bot: 4.0   𓂃    ©  \n"
        "/    づ♡ ♡  Author: Sofian-n  °  𓂃 ࣪ ˖  ִֶָ𐀔\n"
        "==============================\n",
        parse_mode='Markdown',
        reply_markup=keyboard
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

