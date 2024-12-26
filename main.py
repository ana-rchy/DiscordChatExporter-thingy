import sys
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{dir_path}/token.txt", "r") as f:
    TOKEN = f.read()

# randint is a hacky fix for having logs that happen on the same date range
COMMAND = f"discord-chat-exporter-cli export --media --reuse-media -o '%G - %C - (%a to %b) - ({random.randint(0, 9999999)}).html' --media-dir .assets"

def two_args():
    splits_from = sys.argv[1].split("/")
    splits_to = sys.argv[2].split("/")

    if (splits_from[5] != splits_to[5]):
        print("channel ids must match")
        return

    channel_id = splits_from[5]
    msg_id_from = splits_from[6]
    msg_id_to = splits_to[6]

    os.system(f"{COMMAND} -t '{TOKEN}' -c '{channel_id}' --after {msg_id_from} --before {msg_id_to}")

def three_args():
    channel_id = sys.argv[1]
    msg_id_from = sys.argv[2]
    msg_id_to = sys.argv[3]

    os.system(f"{COMMAND} -t '{TOKEN}' -c '{channel_id}' --after {msg_id_from} --before {msg_id_to}")

if (len(sys.argv) == 3):
    two_args()
elif (len(sys.argv) == 4):
    three_args()
else:
    print("wrong number of args")
