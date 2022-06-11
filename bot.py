from http.client import HTTPSConnection
import sys
from json import dumps
from time import sleep

channel_id = "Channel_ID"
server_id = "Server_ID"
token = "Authentification_Token"
message = "Your Message"
#Message repeat in seconds
repeat = 60


header_data = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "authorization": f"{token}",
    "host": "discordapp.com",
    "referrer": f"https://discord.com/channels/{server_id}/{channel_id}"
}

print("Messages will be sent to " + header_data["referrer"] + ".")

def get_connection():
    return HTTPSConnection("discordapp.com", 443)


def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("Message sent!")
            pass

        else:
            sys.stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n")
            pass

    except:
        sys.stderr.write("Failed to send_message\n")
        for key in header_data:
            print(key + ": " + header_data[key])


def main(msg):
    message_data = {
        "content": msg,
        "tts": "false",
    }

    send_message(get_connection(), channel_id, dumps(message_data))


if __name__ == '__main__':
    print()
    value=True
    while(value):
        main(message)
        sleep(repeat)
        

