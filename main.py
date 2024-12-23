import sys
import os

with open("token.txt", "r") as f:
    TOKEN = f.read()

def two_args():
    splits_from = sys.argv[1].split("/")
    splits_to = sys.argv[2].split("/")

    if (splits_from[5] != splits_to[5]):
        print("channel ids must match")
        return

    channel_id = splits_from[5]
    msg_id_from = splits_from[6]
    msg_id_to = splits_to[6]

    os.system(f"discord-chat-exporter-cli export -t '{TOKEN}' -c '{channel_id}' --after {msg_id_from} --before {msg_id_to} --media --reuse-media -o . --media-dir .assets")

def three_args():
    channel_id = sys.argv[1]
    msg_id_from = sys.argv[2]
    msg_id_to = sys.argv[3]

    os.system(f"discord-chat-exporter-cli export -t '{TOKEN}' -c '{channel_id}' --after {msg_id_from} --before {msg_id_to} --media --reuse-media -o . --media-dir .assets")

if (len(sys.argv) == 3):
    two_args()
elif (len(sys.argv) == 4):
    three_args()
else:
    print("wrong number of args")
