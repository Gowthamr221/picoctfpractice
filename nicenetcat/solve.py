fileobj = open("cipher.txt",'r')

lines = fileobj.readlines()
for line in lines:
	
	print(chr(int(line.rstrip())),end="")

fileobj.close()