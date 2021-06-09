import socket
import threading
import sys
from datetime import datetime
import platform
import subprocess
from subprocess import PIPE, Popen

def connect(ip, port, output):
	# create socket object
	obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	socket.setdefaulttimeout(2)
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
		for i in range(main.MAX_ports):
			t = threading.Thread(target=connect, args=(host, i, output))
			threads.append(t)
	
		# start threads
		for i in range(main.MAX_ports):
			threads[i].start()

		# lock main thread until all threads finish
		for i in range(main.MAX_ports):
			threads[i].join()

		for i in range(main.MAX_ports):
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
			main.MAX_ports = 1000
		else:
			subprocess.call('clear', shell=True)

			# check the limit of open file descriptors 
			command = "ulimit -n"
			with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
				# store in a constant
				max_ports = int(process.communicate()[0].decode("utf-8"))
				main.MAX_ports = max_ports - 100

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
[*] # of ports to scan: {main.MAX_ports}
[*] Please wait...
			''')
			scan(host)
			break

if __name__ == "__main__":
	main()