import subprocess
import logging
import sys

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def create_ssh(username, password, expiry_days):
    # Call the Bash script to create SSH WebSocket account
    result = subprocess.run(['usernew', username, password, expiry_days], capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        logger.error(f'Error: {result.stderr}')
        return f'Error: {result.stderr}'
    
    # Read log file
    try:
        with open('/etc/log-create-ssh-clean.log', 'r') as file:
            log_content = file.read()
        return f'SSH WebSocket Account created:\n\n{log_content}'
    except FileNotFoundError:
        logger.error('Log file not found.')
        return 'Log file not found.'

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 ssh.py <username> <password> <expiry_days>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    expiry_days = sys.argv[3]

    output = create_ssh(username, password, expiry_days)
    print(output)
