import socket
import time
#
#
#
# When running in docker we need to waith untill the ports are open before we can connect our app.
#
#
def wait_net_service(server, port, timeout=None):
	"""
	"""
	s = socket.socket()
	s.settimeout(3)

	s=socket.socket()
	while True:
		time.sleep(5)
		try:
			s.connect((server,port))
			return
		except Exception,e:
			print "failed to connec to %s:%s "%(address,port)
			pass
