from socket import *
import sys
if len(sys.argv)<3:
	print("""argv is error
run as
python3 udp_client.py 127.0.0.1 9999""")
	raise
host=sys.argv[1]
port=int(sys.argv[2])#获取的是个字符串型，得转成整形，圈起来要考的!!!
addr=(host,port)
sockfd=socket(AF_INET,SOCK_DGRAM)
while True:
	m=input("发送>>")
	if not m:
		break
	sockfd.sendto(m.encode(),addr)
	data,addr=sockfd.recvfrom(1024)
	print("receive from %s:%s"%(addr,data.decode()))
sockfd.close()