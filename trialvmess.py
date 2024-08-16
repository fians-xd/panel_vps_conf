#!/usr/bin/env python3

import subprocess
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def create_vmess_account():
    try:
        # Call the shell script to create Vmess account
        result = subprocess.run(['trialvmess'], capture_output=True, text=True)
        
        if result.returncode != 0:
            logger.error(f'Error creating Vmess account: {result.stderr}')
            return f'Error: {result.stderr}'
        
        # Read clean log for Telegram
        try:
            with open('/etc/log-create-vmess-trial-clean.log', 'r') as file:
                log_content = file.read()
            return f'Vmess Account created:\n\n{log_content}'
        except FileNotFoundError:
            logger.error('Log file not found.')
            return 'Log file not found.'

    except Exception as e:
        logger.error(f'Unexpected error: {str(e)}')
        return f'Unexpected error: {str(e)}'

if __name__ == '__main__':
    # No need for command-line arguments
    result_message = create_vmess_account()
    print(result_message)
