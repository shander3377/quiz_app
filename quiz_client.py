import socket
from threading import Thread
nick = str(input("Enter your nickname: "))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_Address= "127.0.0.1"
port= 8000
client.connect((ip_Address, port))

def recieve():
    while(True):
        try:
            msg = client.recv(2048).decode("utf-8")
            if msg.lower() == "nickname":
                client.send(nick.encode("utf-8"))
            else:
                print(msg)
        except:
            print("An error occured")
            client.close()
            break;
def write():
    while(True):
        msg = str(input())
        client.send(msg.encode("utf-8"))

while(True):
    recieve_thread = Thread(target=recieve)
    write_thread = Thread(target=write)
    recieve_thread.start()
    write_thread.start()
