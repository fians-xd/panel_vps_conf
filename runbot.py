import logging
import subprocess
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_credentials():
    with open('ver.txt', 'r') as file:
        token = file.readline().strip()
    return token

# Define states for conversation
USERNAME, PASSWORD, EXPIRY = range(3)

# Store user data
user_data = {}

async def menu(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Buat SSH", callback_data='buat_ssh')],
        [InlineKeyboardButton("Buat VMess", callback_data='buat_vmess')],
        [InlineKeyboardButton("Buat VLess", callback_data='buat_vless')],
        [InlineKeyboardButton("Buat Trojan", callback_data='buat_trojan')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    pesan = """
===========================
   👨‍💻 Panel Admin Config 👨‍💻
===========================
=============================
    💠 Versi Boot: 1.0 
    💠 Author: @Sofian
============================="""
    await update.message.reply_text(pesan, reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    script_map = {
        'buat_ssh': 'start_ssh_creation',
        'buat_vmess': 'start_vmess_creation',
        'buat_vless': 'start_vless_creation',
        'buat_trojan': 'start_trojan_creation'
    }

    action = script_map.get(query.data)
    if action == 'start_ssh_creation':
        user_data[query.from_user.id] = {'action': 'start_ssh_creation'}
        await query.edit_message_text(text="Please provide a username for the SSH WebSocket account:")
        return USERNAME
    elif action == 'start_vmess_creation':
        user_data[query.from_user.id] = {'action': 'start_vmess_creation'}
        await query.edit_message_text(text="Please provide a username for the VMess account:")
        return USERNAME
    elif action == 'start_vless_creation':
        user_data[query.from_user.id] = {'action': 'start_vless_creation'}
        await query.edit_message_text(text="Please provide a username for the VLess account:")
        return USERNAME
    elif action == 'start_trojan_creation':
        user_data[query.from_user.id] = {'action': 'start_trojan_creation'}
        await query.edit_message_text(text="Please provide a username for the Trojan account:")
        return USERNAME
    else:
        await query.edit_message_text(text="Action not implemented.")
        return ConversationHandler.END

async def handle_username(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_data[user_id]['username'] = update.message.text
    
    if 'action' in user_data[user_id]:
        if user_data[user_id]['action'] == 'start_ssh_creation':
            await update.message.reply_text('Please provide a password for the SSH WebSocket account:')
            return PASSWORD
        elif user_data[user_id]['action'] == 'start_vmess_creation':
            await update.message.reply_text('Please provide the expiry date (in days) for the VMess account:')
            return EXPIRY
        elif user_data[user_id]['action'] == 'start_vless_creation':
            await update.message.reply_text('Please provide the expiry date (in days) for the VLess account:')
            return EXPIRY
        elif user_data[user_id]['action'] == 'start_trojan_creation':
            await update.message.reply_text('Please provide the expiry date (in days) for the Trojan account:')
            return EXPIRY

async def handle_password(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_data[user_id]['password'] = update.message.text
    await update.message.reply_text('Please provide the expiry date (in days) for the SSH WebSocket account:')
    return EXPIRY

async def handle_expiry(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    expiry_days = update.message.text
    username = user_data[user_id].get('username')

    if 'action' in user_data[user_id]:
        if user_data[user_id]['action'] == 'start_ssh_creation':
            password = user_data[user_id].get('password')
            args = ['python3', 'ssh.py', username, password, expiry_days]
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            logging.info(f"Process output: {stdout.decode()}")
            logging.error(f"Process error: {stderr.decode()}")

            if process.returncode == 0:
                await update.message.reply_text(f"SSH WebSocket Account created:\n\n{stdout.decode()}")
            else:
                await update.message.reply_text(f"Error while creating SSH WebSocket account:\n{stderr.decode()}")
        elif user_data[user_id]['action'] == 'start_vmess_creation':
            args = ['python3', 'vmess.py', username, expiry_days]
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            logging.info(f"Process output: {stdout.decode()}")
            logging.error(f"Process error: {stderr.decode()}")

            if process.returncode == 0:
                await update.message.reply_text(f"VMess Account created:\n\n{stdout.decode()}")
            else:
                await update.message.reply_text(f"Error while creating VMess Account:\n{stderr.decode()}")
        elif user_data[user_id]['action'] == 'start_vless_creation':
            args = ['python3', 'vless.py', username, expiry_days]
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            logging.info(f"Process output: {stdout.decode()}")
            logging.error(f"Process error: {stderr.decode()}")

            if process.returncode == 0:
                await update.message.reply_text(f"VLess Account created:\n\n{stdout.decode()}")
            else:
                await update.message.reply_text(f"Error while creating VLess Account:\n{stderr.decode()}")
        elif user_data[user_id]['action'] == 'start_trojan_creation':
            args = ['python3', 'trojan.py', username, expiry_days]
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            logging.info(f"Process output: {stdout.decode()}")
            logging.error(f"Process error: {stderr.decode()}")

            if process.returncode == 0:
                await update.message.reply_text(f"Trojan Account created:\n\n{stdout.decode()}")
            else:
                await update.message.reply_text(f"Error while creating Trojan Account:\n{stderr.decode()}")

    return ConversationHandler.END

def main():
    token = load_credentials()
    application = Application.builder().token(token).build()

    conversation_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button, pattern='^buat_ssh|buat_vmess|buat_trojan|buat_vless$')],
        states={
            USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_username)],
            PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_password)],
            EXPIRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_expiry)]
        },
        fallbacks=[],
    )

    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(conversation_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
