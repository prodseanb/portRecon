import socket
import subprocess
import platform
import sys
from datetime import datetime


if platform.system() == "Windows":
	subprocess.call('cls', shell=True)
else:
	subprocess.call('clear', shell=True)

while True:	
	# extract target's hostname
	host = input("Remote host to scan: ")
	# allow user to quit
	quit = ['q', 'quit' 'exit', 'x', 'close']
	if host in quit:
		sys.exit()
	# continue if input isnt empty
	elif host != "":
		print(f"\n[TARGET] ==> {host}")
		ip = socket.gethostbyname(host) 

		print(f'''
/***
*                      _                                           
*     _ __   ___  _ __| |_     ___  ___ __ _ _ __  _ __   ___ _ __ 
*    | '_ \ / _ \| '__| __|   / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
*    | |_) | (_) | |  | |_    \__ \ (_| (_| | | | | | | |  __/ |   
*    | .__/ \___/|_|   \__|___|___/\___\__,_|_| |_|_| |_|\___|_|   
*    |_|                 |_____|                                   
*
*	@Author: prodseanb
*	@GitHub: https://github.com/prodseanb 
*
*/

[*] Scanning: {ip}
[*] Please wait...
		''')

		time1 = datetime.now()

		try:
			# scan ports (specify the range)
			for port in range(0,5555):
				# create socket object
				obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
			
				# error indicator
				result = obj.connect_ex((ip,port))
				if result == 0: # print open ports
					try: # get the service name
						serv = socket.getservbyport(port)
					except socket.error:
						serv = "none"
					
					print(f"[Hit] {ip}:{port} = OPEN        [*] SERVICE: {serv}")
				obj.close()

		except KeyboardInterrupt:
			print("\n[Ign] Keyboard Interrupt -- Exiting.")
			sys.exit()
		except socket.gaierror:
			print("\n[Err] Hostname could not be resolved.")
			sys.exit()
		except socket.error:
			print("\n [Err] Server could not be reached.")
			sys.exit()
		# Calculate how long it took to scan
		time2 = datetime.now()
		period = time2 - time1
		# get os, os version, name, etc.
		#name = platform.uname(ip)
		#print(name)
		print(f"Time taken: {period}")
		break
	else:
		continue