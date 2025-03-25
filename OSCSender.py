from pythonosc.udp_client import SimpleUDPClient
import time

ip = "192.168.0.51"
port = 8000
# global last_pose


def main(values):
    send_message(values['poses'])

  

def send_message(message):
    client = SimpleUDPClient(ip, port)
    client.send_message("/my_address", message)
    # time.sleep(5)