import socket
from handlers import HANDLERS
from services import create_check_dict,load_data

# TCP Connection to emulator
HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

# Loads or creates a savefile
check_list = load_data()
if not check_list:
    print("loading failed")
    check_list = create_check_dict()


print(f"Listening on {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"Connected by {addr}")

matching_scene = ""

# recieves the data and processes it to current location
with conn:
    while True:
        try:
            data = conn.recv(1024).decode().strip()
        except:
            print("Connection failed")
            break

        values = {}
        data_split = data.split("|")
        state = data_split[0]
        for item in data_split[1:]:
            key, value = item.split("=", 1)
            values[key] = value

        if not data:
            break

        matching_scene = HANDLERS[state](values,matching_scene)



print("Connection closed.")