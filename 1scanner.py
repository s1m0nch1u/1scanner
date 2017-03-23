import socket

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	portList = [21,22,25,80,110,443,3306,3389,8000,8080,8888]
	for x in range(1,255):
		ip = '192.168.0.' + str(x)
		print 'scanning: ' + ip + ' >>>>>>'
		for port in portList:
			banner = retBanner(ip, port)
			if banner:
				print '[+] ' + ip + ':' + str(port) + ': ' + banner

if __name__ == '__main__':
	main()
