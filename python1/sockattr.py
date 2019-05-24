from socket import *
s=socket()
s.bind(("192.168.80.128",9999))
print(s.family)
print(s.type)
print(s.getsockname())
print(s.fileno())
s.listen(5)
while 1:
	c,addr=s.accept()
	print(c.getpeername())