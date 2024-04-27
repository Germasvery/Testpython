import base64
import asyncio
from telethon import TelegramClient
import getpass

api_id = "26349381"
api_hash = "068bf97ef9dff3138e897de2665f2fd6"

def check_password():
    password = getpass.getpass("Enter password: ")
    
    valid_password = "7svIRIBi"  # Example valid password
    
    if password == valid_password:
        return True
    else:
        print("Incorrect password. Please try again.")
        return False

def check_password():
    password = getpass.getpass("Enter password: ")
    
    valid_password = "7svIRIBi"
    
    if password == valid_password:
        return True
    else:
        print("Incorrect password. Please try again.")
        return False

client = TelegramClient('my_account', api_id, api_hash)

async def main():
    await client.start()

if __name__ == '__main__':
    if check_password():
        asyncio.get_event_loop().run_until_complete(main())
