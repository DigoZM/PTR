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

import pyRTOS
from random import randint
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


# User defined message types start at 128
REQUEST_DATA = 128  #from sample
SENT_DATA = 129     #from sample
FLIGHT_REQUEST = 130
SENT_FLIGHT = 131
FLIGHT_REQUEST_BACK = 132
SENT_FLIGHT_BACK = 133
WAIT_NORMALIZATION = 134

# global variables
ARRIVAL = 1.5
flight_zone = [0, 0, 0] # [0, 0, 0] três zonas
wait_list = []
target_drones = []
drones_handle = []
drones_start = [1, 2, 3, 4, 5]
drones_fly = []
drones_end = []
ZONE_Z = [1, 2, 3]
number_drones = 5
Execution_times_listen_request = []
Execution_times_manage_flight_zones = []
Execution_times_wait_list = []
Execution_times_fly = []
Execution_times_emergency_button = []

def get_target_position(target):
    #print(target)
    code, (x, y, z) = sim.simxGetObjectPosition(clientID, target_drones[target], -1, sim.simx_opmode_streaming)
    while code != 0:
        code, (x, y, z) = sim.simxGetObjectPosition(clientID, target_drones[target], -1, sim.simx_opmode_buffer)
        #print(code, x, y, z)
    return x, y, z
    
def get_drone_position(drone):

    code, (x, y, z) = sim.simxGetObjectPosition(clientID, drones_handle[drone], -1, sim.simx_opmode_streaming)
    while code != 0:
        code, (x, y, z) = sim.simxGetObjectPosition(clientID, drones_handle[drone], -1, sim.simx_opmode_buffer)
        #print(code, x, y, z)
    return x, y, z
    
# self is the thread object this runs in

def task_listen_request(self):
    ### Setup code here


    ### End Setup code

    # Pass control back to RTOS
    yield

    # Thread loop
    while True:
        start_time = time.time()

        # Check messages
        #print("task_listen_request")
        msgs = self.recv()
        for msg in msgs:

            ### Handle messages by adding elifs to this
            if msg.type == FLIGHT_REQUEST: 

                #print("Requisição de voô:", self.name)
                #print("Requested by:", msg.message)
                self.send(pyRTOS.Message(SENT_FLIGHT, self, "task_manage_flight_zones", msg.message))
            if msg.type == FLIGHT_REQUEST_BACK: 

                #print("Requisição de voô:", self.name)
                #print("Requested by:", msg.message)
                self.send(pyRTOS.Message(SENT_FLIGHT_BACK, self, "task_manage_flight_zones", msg.message))

                
                
            ### End Message Handler

        ### Work code here
        



        ### End Work code
        listen_request_time = time.time()-start_time
        if(listen_request_time!=0):
            Execution_times_listen_request.append(listen_request_time)
        yield [pyRTOS.wait_for_message(self), pyRTOS.timeout(0.1)]


def task_manage_flight_zones(self):

    ### Setup code here

    ### End Setup code

    # Pass control back to RTOS
    yield

    # Thread loop
    while True:
        start_time = time.time()

        # Check messages
        #print("task_manage_flight_zones")
        msgs = self.recv()
        for msg in msgs:

            ### Handle messages by adding elifs to this
            if msg.type == SENT_FLIGHT: 
                free_zone = False
                for i in range(len(flight_zone)):
                    if(flight_zone[i] == 0):
                        #Levanta voo pra altura da zona
                        drone = int(msg.message)
                        x, y, z = get_target_position(drone)
                        code = -1
                        while (code != 0):                    
                            code = sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y, ZONE_Z[i]), sim.simx_opmode_oneshot) 
                        #print(code)
                        #time.sleep(2)
                        print("Zona livre: ", i)
                        flight_zone[i] = drone
                        print("Flight Zone: ", flight_zone)
                        free_zone = True
                        break
                if(not free_zone):
                    #Colocar drone em lista de espera
                    wait_list.append(msg.message)
                    print("Todas as zonas ocupadas\nEspera: ", wait_list)
            if msg.type == SENT_FLIGHT_BACK: 
                free_zone = False
                for i in range(len(flight_zone)):
                    if(flight_zone[i] == 0):
                        #Levanta voo pra altura da zona
                        drone = int(msg.message)
                        x, y, z = get_target_position(drone)
                                              
                        code = sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y, ZONE_Z[i]), sim.simx_opmode_oneshot) 
                        #print(code)
                        #time.sleep(2)
                        print("Zona livre: ", i)
                        flight_zone[i] = -drone
                        print("Flight Zone: ", flight_zone)
                        free_zone = True
                        break
                if(not free_zone):
                    #Colocar drone em lista de espera
                    wait_list.append("-{}".format(msg.message))
                    print("Todas as zonas ocupadas\nEspera: ", wait_list)


                
                
            ### End Message Handler

        ### Work code here
        



        ### End Work code
        manage_flight_zones_time = time.time()-start_time
        if(manage_flight_zones_time!=0.0):
            Execution_times_manage_flight_zones.append(manage_flight_zones_time)
        yield [pyRTOS.wait_for_message(self), pyRTOS.timeout(1)]


def task_wait_list(self):
    ### Setup code here

    ### End Setup code

    # Pass control back to RTOS
    yield

    # Thread loop
    while True:
        start_time = time.time()
        #print("task_wait_list")
        if(len(wait_list) != 0):
            for i in range(len(flight_zone)):
                if(flight_zone[i] == 0):
                    drone = int(wait_list[0])
                    x, y, z = get_target_position(abs(drone))
                    code = sim.simxSetObjectPosition(clientID, target_drones[abs(drone)], -1, (x, y, ZONE_Z[i]), sim.simx_opmode_oneshot) 
                    print(code)
                    print("Zona livre: ", i)
                    flight_zone[i] = drone
                    wait_list.pop(0)
                    print("Flight Zone: ", flight_zone)
                    free_zone = True
                    break
        wait_list_time = time.time()-start_time
        if(wait_list_time!=0.0):
            Execution_times_wait_list.append(wait_list_time)
        yield [pyRTOS.timeout(1)]

def task_fly(self):
    ### Setup code here
    count = 0
    ### End Setup code

    # Pass control back to RTOS
    yield

    # Thread loop
    while True:
        start_time = time.time()
        for i in range(len(flight_zone)):
            drone = flight_zone[i]
            signal = 1
            if(drone < 0):
                signal = -1
            drone = abs(drone)
            if(drone != 0):
                x, y, z = get_target_position(drone)
                #se pos atual = fim:
                if((y > ARRIVAL and signal == 1) or (y < -ARRIVAL and signal == -1)):      #land drone
                    print("CHEGOU O ", drone)
                    #time.sleep(2)
                    sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y, 0.2), sim.simx_opmode_oneshot) 
                    if(signal == 1):
                        drones_end.append(drone)
                    else:
                        drones_start.append(drone)
                    flight_zone[i] = 0
                    count = 0
                else:
                #fazer pos em x ou y + distancia
                    #time.sleep(2)
                    sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y+(1*signal), ZONE_Z[i]), sim.simx_opmode_oneshot) 
                    count += 1
                    print("Drone ", flight_zone[i], " pos ", y)
        fly_time = time.time()-start_time
        if fly_time!=0.0:
            Execution_times_fly.append(fly_time)
        yield [pyRTOS.timeout(2.5)]

def emergency_button(self):
    ### Setup code here
    #sim.simxGetInt32Signal(clientID, "myButton", sim.simx_opmode_streaming)


    ### End Setup code

    # Pass control back to RTOS
    yield

    # Thread loop
    while True:
        start_time = time.time()
        #Se o botao for apertado
        code, button = sim.simxGetInt32Signal(clientID, "myButton", sim.simx_opmode_buffer)
        print("BOTAO: ", button)
        if(button == 1):
            #espera o botao ser apertado novamente
            self.send(pyRTOS.Message(WAIT_NORMALIZATION, self, "normalization"))
            # for i in range(1, number_drones+1):
            #     #manda o drone voltar para o inicio
            #     x, y, z = get_target_position(i)
            #     #time.sleep(2)
            #     sim.simxSetObjectPosition(clientID, target_drones[i], -1, (x, -2, 0.2), sim.simx_opmode_oneshot) 
            #     print("drone voltando: ", i)
            #     drones_start = [1, 2, 3, 4, 5]
            #     drones_end = []
            # for i in range(len(flight_zone)):
            #     flight_zone[i] = 0

            # time.sleep(5)


        emergency_button_time = time.time() -start_time
        if emergency_button_time !=0.0:
            Execution_times_emergency_button.append(emergency_button_time)
        yield [pyRTOS.timeout(0.5)]


def normalization(self):
### Setup code here


    ### End Setup code

    # Pass control back to RTOS
    yield

    # Thread loop
    while True:
        normalized = False
        # Check messages
        #print("task_listen_request")
        msgs = self.recv()
        for msg in msgs:

            ### Handle messages by adding elifs to this
            if msg.type == WAIT_NORMALIZATION: 
                code, button = sim.simxGetInt32Signal(clientID, "myButton", sim.simx_opmode_buffer)  
                while(button == 1):
                    code, button = sim.simxGetInt32Signal(clientID, "myButton", sim.simx_opmode_buffer)
                normalized = True

        if(normalized):
            print(flight_zone)
            print(drones_end)
            print(wait_list)
            # drones_back_emergency = []
            # for i in range(len(flight_zone)):
            #     if(flight_zone[i] != 0):
            #         drones_back_emergency.append(flight_zone[i])
            # for i in range(len(drones_end)):
            #     drones_back_emergency.append(drones_end[i])
            # for i in range(len(wait_list)):
            #     drones_back_emergency.append(abs(int(wait_list[i])))
            # print(drones_back_emergency)
            # for i in range(len(drones_back_emergency)):
            #     drone = drones_back_emergency[i]
            #     print( "Voltando: ", drone)
            #     while(True):
            #         x, y, z = get_target_position(drone)
            #         if(y < -ARRIVAL):
            #             print(drone, " chegou em ", y)
            #             break
            #         sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y-1, ZONE_Z[0]), sim.simx_opmode_oneshot)
            #         posx, posy, posz = get_drone_position(drone)
            #         print(posx, posy, posz)
            #         while(abs(abs(posy) - abs(y-1)) > 0.1):
            #             posx, posy, posz = get_drone_position(drone)
            
            for i in range(len(flight_zone)):
                if(flight_zone[i] != 0):
                    drone = abs(flight_zone[i])
                    while(True):
                        x, y, z = get_target_position(drone)
                        if(y < -ARRIVAL):
                            print(drone, " chegou em ", y)
                            break
                        sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y-1, ZONE_Z[i]), sim.simx_opmode_oneshot)
                        flight_zone[i] = 0
                        posx, posy, posz = get_drone_position(drone)
                        print(posx, posy, posz)
                        while(abs(abs(posy) - abs(y-1)) > 0.1):
                            posx, posy, posz = get_drone_position(drone)
                        print("chegou:", posy, " ", posz )
            for i in range(len(drones_end)):
                drone = drones_end[i]
                y = 2
                while(True):
                    x, y, z = get_target_position(drone)
                    if(y < -ARRIVAL):
                        break
                    sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y-1, ZONE_Z[0]), sim.simx_opmode_oneshot)
                    posx, posy, posz = get_drone_position(drone)
                    while(abs(abs(posy) - abs(y-1)) > 0.05):
                        posx, posy, posz = get_drone_position(drone)
            for i in range(len(wait_list)):
                drone = abs(int(wait_list[i]))
                y = 2
                while(True):
                    x, y, z = get_target_position(drone)
                    if(y < -ARRIVAL):
                        print(drone, " chegou em ", y)
                        break
                    sim.simxSetObjectPosition(clientID, target_drones[drone], -1, (x, y-1, ZONE_Z[0]), sim.simx_opmode_oneshot)
                    posx, posy, posz = get_drone_position(drone)
                    while(abs(abs(posy) - abs(y-1)) > 0.05):
                        posx, posy, posz = get_drone_position(drone)
            #         #time.sleep(2)#############################################
            drones_start.clear()
            drones_start.append(1)
            drones_start.append(2)
            drones_start.append(3)
            drones_start.append(4)
            drones_start.append(5)
            drones_end.clear()
            wait_list.clear()
            print(drones_start)
            #drones_end=[]
            for i in range(len(drones_start)):
                x, y, z = get_target_position(drones_start[i])
                sim.simxSetObjectPosition(clientID, target_drones[drones_start[i]], -1, (x, y, 0.2), sim.simx_opmode_oneshot)    
                posx, posy, posz = get_drone_position(drones_start[i])
                while(abs(abs(posz) - 0.2) > 0.15):
                    posx, posy, posz = get_drone_position(drones_start[i])
      



                

                
                
            ### End Message Handler

        ### Work code here
        



        ### End Work code
        
        yield [pyRTOS.wait_for_message(self), pyRTOS.timeout(0.07)]    

def task_random_drones(self):
    ### Setup code here
    


    ### End Setup code

    # Pass control back to RTOS
    yield

    # Thread loop
    while True:

        
        ### Work code here
        #Select random drone and send request to fly
        if(len(drones_start) != 0):
            drone = drones_start[randint(0, len(drones_start)-1)]
            self.send(pyRTOS.Message(FLIGHT_REQUEST, self, "task_listen_request", str(drone)))
            drones_start.remove(drone)
            drones_fly.append(drone)
            print("<Drone> ", drone)
        if(len(drones_end) != 0):
            drone = drones_end[randint(0, len(drones_end)-1)]
            self.send(pyRTOS.Message(FLIGHT_REQUEST_BACK, self, "task_listen_request", str(drone)))
            drones_end.remove(drone)
            drones_fly.append(drone)
            print("<Drone> ", -drone)


        ### End Work code

        yield [pyRTOS.timeout(3)]
        
def task_print_times(self):
    yield
    while True:

        print("-----------------------------------------------")
        print("MFZ: ",Execution_times_manage_flight_zones)
        print("WL: ",Execution_times_wait_list)
        print("Fly: ",Execution_times_fly)
        print("LR: ",Execution_times_listen_request)
        print("EB: ",Execution_times_emergency_button)
        print("-----------------------------------------------")
        Tempos=open("Tempos.txt","w")
        Tempos.write("Mange_Flight_Zones:\n-------------------\n")
        for x in Execution_times_manage_flight_zones:
            Tempos.write(str(x) + "\n")
        Tempos.write("Wait_list:\n-------------------\n")
        for x in Execution_times_wait_list:
            Tempos.write(str(x) + "\n")
        Tempos.write("Fly:\n-------------------\n")
        for x in Execution_times_fly:
            Tempos.write(str(x) + "\n")
        Tempos.write("Listen:\n-------------------\n")
        for x in Execution_times_listen_request:
            Tempos.write(str(x) + "\n")
        Tempos.write("Button:\n-------------------\n")
        for x in Execution_times_emergency_button:
            Tempos.write(str(x) + "\n")

        Tempos.close()
        yield[pyRTOS.timeout(1)]



pyRTOS.add_task(pyRTOS.Task(emergency_button, priority=1, name="emergency_button", notifications=None, mailbox=True))
pyRTOS.add_task(pyRTOS.Task(normalization, priority=1, name="normalization", notifications=None, mailbox=True))
pyRTOS.add_task(pyRTOS.Task(task_listen_request, priority=2, name="task_listen_request", notifications=None, mailbox=True))
pyRTOS.add_task(pyRTOS.Task(task_wait_list, priority=3, name="task_wait_list", notifications=None, mailbox=True))
pyRTOS.add_task(pyRTOS.Task(task_manage_flight_zones, priority=4, name="task_manage_flight_zones", notifications=None, mailbox=True))
pyRTOS.add_task(pyRTOS.Task(task_fly, priority=5, name="task_fly", notifications=None, mailbox=True))


pyRTOS.add_task(pyRTOS.Task(task_random_drones, priority=2, name="task_random_drones", notifications=None, mailbox=True))
#pyRTOS.add_service_routine(lambda: print(""))
pyRTOS.add_task(pyRTOS.Task(task_print_times,priority=1,name="task_print_times",notifications=None,mailbox=True))







print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')
    target_drones.append(0)
    drones_handle.append(0)
    for i in range((number_drones)):
        code, handleTarget = sim.simxGetObjectHandle(clientID, "/target[{}]".format(i), sim.simx_opmode_blocking)
        code, droneHandle = sim.simxGetObjectHandle(clientID, "/Quadcopter[{}]".format(i), sim.simx_opmode_blocking)
        print(code, handleTarget)
        target_drones.append(handleTarget)
        drones_handle.append(droneHandle)
    print(target_drones)
    sim.simxGetInt32Signal(clientID, "myButton", sim.simx_opmode_streaming)
    pyRTOS.start()
    

    # Now send some data to CoppeliaSim in a non-blocking fashion:
    sim.simxAddStatusbarMessage(clientID,'Hello CoppeliaSim!',sim.simx_opmode_oneshot)

    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
