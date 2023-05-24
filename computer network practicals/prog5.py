from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)

   s = socket(AF_INET, SOCK_DGRAM)
   i=5353
   s.bind((t_IP,i))
   conn = s.recvfrom((i))
   print(conn)
   if(conn != None):
      print ('Port %d: OPEN' % (i,))
   else:
      print('Port is closed')
      s.close()
print('Time taken:', time.time() - startTime)
