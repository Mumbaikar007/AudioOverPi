import socket
import os

HOST = ''
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 530960

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print ('listening ...')

while True:
  conn, addr = serv.accept()
  print ('client connected ... ', addr)
  

  while True:
    data = conn.recv(BUFSIZE)
    if not data: break
    #myfile.write(data.decode("0xff") )
    with open('testfile6.wav', 'wb') as f :
      f.write(data)

    
    print ('writing file ....')
  f.close()
  #myfile.close()
  print ('finished writing file')
  conn.close()
  print ('client disconnected')


  os.system('omxplayer -o local testfile6.wav')
