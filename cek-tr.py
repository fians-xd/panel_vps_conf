#!/usr/bin/env python3

import subprocess
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def cek_trojan():
    try:
        # Call the Bash script to create SSH WebSocket account
        result = subprocess.run(['cek-tr'], capture_output=True, text=True)
        
        if result.returncode != 0:
            logger.error(f'Error User Login Trojan Account: {result.stderr}')
            return f'Error: {result.stderr}'
        
        # Read log file
        try:
            with open('/etc/cek-tr.log', 'r') as file:
                log_content = file.read()
            return f'{log_content}'
        except FileNotFoundError:
            logger.error('Log file not found.')
            return 'Log file not found.'

    except Exception as e:
        logger.error(f'Unexpected error: {str(e)}')
        return f'Unexpected error: {str(e)}'

if __name__ == '__main__':
    # No need for command-line arguments
    result_message = cek_trojan()
    print(result_message)
