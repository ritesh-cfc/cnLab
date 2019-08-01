#
import socket

ip = "192.168.41.171"
port = 5056
i=0
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(100):
	inp_str= input()
	s.sendto(inp_str.encode(),(ip,port))
	
s.close()
