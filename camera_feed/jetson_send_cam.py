import cv2
import socket
import struct
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.10.10.10', 8089))

cap = cv2.VideoCapture(0)
# Lowering resolution improves stability over the simulated 2.4GHz link
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Streaming to PC...")

try:
    while True:
        ret, frame = cap.read()
        if not ret: break
            
        data = pickle.dumps(frame)
        # 'Q' ensures we are sending an 8-byte size header
        message = struct.pack("Q", len(data)) + data
        client_socket.sendall(message)
except:
    print("Stopping Stream")
finally:
    cap.release()
    client_socket.close()
