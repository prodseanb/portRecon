import socket
import threading
import sys
from datetime import datetime
import platform
import subprocess

def connect(ip, port, output):
	# create socket object
	obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	socket.setdefaulttimeout(12)
	try:
		obj.connect((ip, port))
		output[port] = 'Open'
	except:
		output[port] = ''

def scan(host):
	threads = [] # run connect() simultaenously
	output = {}	 # for printing the output

	time1 = datetime.now()

	try:
		# create threads
		subprocess.call('ulimit -n 5000', shell=True) # add more file handles/set to 5000
		for i in range(5000):
			t = threading.Thread(target=connect, args=(host, i, output))
			threads.append(t)

		# start threads
		for i in range(5000):
			threads[i].start()
		# lock main thread until all threads finish
		for i in range(5000):
			threads[i].join()

		for i in range(5000):
			if output[i] == 'Open':
				try: # get the service name
					serv = socket.getservbyport(i)
				except socket.error:
					serv = 'none'
				print('[Hit] ' + host + ':' + str(i) + ' = ' 
					+ output[i] + '        [*] SERVICE: ' + serv)
	except KeyboardInterrupt:
		print("\n[Ign] Keyboard Interrupt -- Exiting...")
		sys.exit()
	except socket.gaierror:
		print("\n[Err] Hostname could not be resolved...")
		sys.exit()
	except socket.error:
		print("\n [Err] Server could not be reached...")
		sys.exit()
	# How long it took to scan
	time2 = datetime.now()
	time_taken = time2 - time1
	print(f"[*] Time taken: {time_taken}")

def main():
	while True:
		# Clear the screen
		if platform.system() == "Windows":
			subprocess.call('cls', shell=True)
		else:
			subprocess.call('clear', shell=True)

		# extract target's hostname -- gonna need this for gethostbyname()
		ip = input("Remote host to scan: ")
		
		# allow user to quit
		quit = ['q', 'quit' 'exit', 'x', 'close']
		if ip in quit:
			sys.exit()
		elif ip == "":
			continue
		elif ip != "":
			# DNS
			host = socket.gethostbyname(ip)
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

[*] Scanning: {host}
[*] Please wait...
			''')
			scan(host)
			break

if __name__ == "__main__":
	main()