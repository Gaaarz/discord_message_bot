import sys
import json
from time import sleep
from http.client import HTTPSConnection
#If you want to use a random sleep
#from random import random

CHANNEL_ID = "Channel_ID"
SERVER_ID = "Server_ID"
TOKEN = "Authentification_Token"
MESSAGE = "Your Message"
REPEAT = 60

HEADER_DATA = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "authorization": TOKEN,
    "host": "discordapp.com",
    "referrer": f"https://discord.com/channels/{SERVER_ID}/{CHANNEL_ID}"
}

print(f"Messages will be sent to {HEADER_DATA['referrer']}.")


def get_connection():
    return HTTPSConnection("discordapp.com", 443)


def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, HEADER_DATA)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("Message sent!")
        else:
            sys.stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n")

    except Exception as e:
        sys.stderr.write(f"Failed to send_message: {e}\n")
        for key, value in HEADER_DATA.items():
            print(f"{key}: {value}")


def main(msg):
    message_data = {
        "content": msg,
        "tts": "false",
    }

    with get_connection() as conn:
        send_message(conn, CHANNEL_ID, json.dumps(message_data))


if __name__ == '__main__':
    print()
    while True:
        main(MESSAGE)
        sleep(REPEAT)
        #Random sleep
        #sleep(random()*2)
