#!/usr/bin/env python3

import subprocess
import sys
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def create_trojan_account(username, expiry_days):
    try:
        # Call the Bash script to create Trojan account
        result = subprocess.run(['add-tr', username, expiry_days], capture_output=True, text=True)
        
        if result.returncode != 0:
            logger.error(f'Error creating Trojan account: {result.stderr}')
            return f'Error: {result.stderr}'
        
        # Read log file
        try:
            with open('/etc/log-create-trojan-clean.log', 'r') as file:
                log_content = file.read()
            return f'Trojan Account created:\n\n{log_content}'
        except FileNotFoundError:
            logger.error('Log file not found.')
            return 'Log file not found.'

    except Exception as e:
        logger.error(f'Unexpected error: {str(e)}')
        return f'Unexpected error: {str(e)}'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 trojan.py <username> <expiry_days>")
        sys.exit(1)

    username = sys.argv[1]
    expiry_days = sys.argv[2]
    result_message = create_trojan_account(username, expiry_days)
    print(result_message)
