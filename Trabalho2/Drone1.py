import socket
import time


def TCPclient(host,port):
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((host,port))
    #status = tcp_client.send(('Hello, world! From '+host+':'+str(port)).encode('utf8'))
    status = tcp_client.send(('Decolar').encode('utf8'))
    if status > 0:
        data = tcp_client.recv(1024)
        print('Saida: ',data.decode('utf8'))

    time.sleep(1)
    status = tcp_client.send(('Aterrisar').encode('utf8'))
    if status > 0:
        data = tcp_client.recv(1024)
        print('Saida: ',data.decode('utf8'))

    tcp_client.close()



TCPclient('localhost',1235)
