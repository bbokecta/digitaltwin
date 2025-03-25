from pythonosc.udp_client import SimpleUDPClient
import time

ip = "10.106.32.214"
port = 8000

def main(values):
    

    pose_names = list(values.keys())
    pose_values = list(values.values())
    pose_results = []
    
    for pose in pose_names:
        if float(values[pose]) > 0.75:
            # print(pose)
            send_message(str(pose))
        
        # print(pose_results[:4])
        
        # if float(values[pose]) > 0.75:
    
        #     # send_message(str(pose))
        #     print(str(pose))
        #     time.sleep(8)
        # else:
        #     print("waiting")
        # else:
        #     print("none")

    # for pose in pose_values:
    #     print(pose_values[pose].keys)

  

def send_message(message):
    client = SimpleUDPClient(ip, port)
    client.send_message("/my_address", message)
    # time.sleep(5)