from socket import *
import os,sys
def LOGIN(s,data2,addr,k):
	if data2[1] not in k and data2[1]!="管理员":
		s.sendto("create success",addr)
	for i in k:
		s.sendto("welcome %s"%(data2[1]),k[i])
	k[data2[1]]=addr
def CHAT(s,addr,data2,k):
		for i in k:
			if i !=data2[1]:
				s.sendto(data2[2:],k[i])

def mao(s):
	k={}
	while True:
		data,addr=s.recvfrom(2048)
		data2=data.decode().split()
		if data2=="L":
			LOGIN(s,data2,addr,k)
		elif data2=="C":
			CHAT(s,addr,data2)
		elif data2=="Q":
			QUIT()
def sky():
	pass
def main():
	addr=("0.0.0.0",8888)
	s=socket(AF_INET,SOCK_DGRAM)
	s.bind(addr)
	pid=os.fork()
	if pid<0:
		sys.exit("failed")
	elif pid==0:
		mao(s)
	else:
		sky()
	