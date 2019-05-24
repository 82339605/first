from socket import *
sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.connect(("127.0.0.1",8888))
while True:
	data=input("发送>>")
	if not data:
		break
	sockfd.send(data.encode())
	data0=sockfd.recv(1024)
	print("接收到:",data0.decode())
sockfd.close()
