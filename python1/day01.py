from socket import *
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",9949))
sockfd.listen(5)
print("wait a minute")
connfd,addr=sockfd.accept()
print("connect from ",addr)
while True:
	data=connfd.recv(1024)
	if not data.decode():
		break	
	print(data.decode())
	n=connfd.send(m.encode())
	print("发送了%d个字节"%n)
connfd.close()
sockfd.close()
