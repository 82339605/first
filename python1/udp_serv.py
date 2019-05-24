from socket import *
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("0.0.0.0",9999))
while True:
	data,addr=sockfd.recvfrom(1024)
	print("receive from %s:%s"%(addr,data.decode()))
	sockfd.sendto("收到你的消息".encode(),addr)
sockfd.close()
