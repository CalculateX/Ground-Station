# turn firewalls off - turn network off
import cv2
import socket
import struct
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 8089))
server_socket.listen(10)
print("Waiting for Jetson connection...")

conn, addr = server_socket.accept()
data = b""
payload_size = struct.calcsize("Q") # Use 'Q' for 8-byte unsigned long long

try:
    while True:
        # 1. Capture the message size header
        while len(data) < payload_size:
            packet = conn.recv(4*1024) # 4KB chunks
            if not packet: break
            data += packet
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        # 2. Capture the actual frame data based on that size
        while len(data) < msg_size:
            data += conn.recv(4*1024)
            
        frame_data = data[:msg_size]
        data = data[msg_size:]

        # 3. Decompress and show
        frame = pickle.loads(frame_data)
        cv2.imshow('Mines Rover Live Feed', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print(f"Stream Error: {e}")
finally:
    cv2.destroyAllWindows()
    conn.close()
