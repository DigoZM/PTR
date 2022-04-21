# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

def TCPserver(host, port, clientID, handleTarget):

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host, port))
    while True:
        tcp_server.listen()
        conn, addr = tcp_server.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if(data.decode('utf8') == 'Decolar'):
                print('Servidor recebeu a mensagem de decolagem')
                code = -1
                while (code != 0):
                    code = sim.simxSetObjectPosition(clientID, handleTarget, -1, (0, 0, 2), sim.simx_opmode_oneshot) 
                data= 'Sucesso'.encode('utf8')
            elif(data.decode('utf8') == 'Aterrisar'):
                print('Servidor recebeu a mensagem de aterrisagem')
                data= 'Sucesso'.encode('utf8')
            else:
                print('Servidor nao recebeu a mensagem correta')
                data='Erro'.encode('utf8')
            conn.sendall(data)
    conn.close()


try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time
import socket

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')
    code = -1
    while (code != 0):
        code, handleTarget = sim.simxGetObjectHandle(clientID, "/target", sim.simx_opmode_blocking)
        print(code, handleTarget)
    while True:
        TCPserver('localhost', 1235, clientID, handleTarget)

    # Now send some data to CoppeliaSim in a non-blocking fashion:
    sim.simxAddStatusbarMessage(clientID,'Hello CoppeliaSim!',sim.simx_opmode_oneshot)

    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')