import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

#Execution_times_listen_request = []
#Execution_times_manage_flight_zones = []
#Execution_times_wait_list = []
#Execution_times_fly = []
#Execution_times_emergency_button = []
#Execution_time_normalization = []

Execution_times_listen_request = []
Execution_times_manage_flight_zones = []
Execution_times_wait_list = []
Execution_times_fly = []
Execution_times_emergency_button = []
Execution_time_normalization = []

listas = [Execution_times_listen_request,Execution_times_manage_flight_zones,Execution_times_wait_list,Execution_times_fly,Execution_times_emergency_button,Execution_time_normalization]
max_values= [max(Execution_times_listen_request),max(Execution_times_manage_flight_zones),max(Execution_times_wait_list),max(Execution_times_fly),max(Execution_times_emergency_button),max(Execution_time_normalization)]
medias = [mean(Execution_times_listen_request),mean(Execution_times_manage_flight_zones),mean(Execution_times_wait_list),mean(Execution_times_fly),mean(Execution_times_emergency_button),mean(Execution_time_normalization)]
labels = ['Listen Request','Manage Flight Zones','Wait List','Fly','Emergency Button','Nomalization']
for i in range(len(listas)):
    print(i,":Tam: ",len(listas[i]))

fig, ax = plt.subplots( nrows=3,ncols=2)


ax[0,0].hist(listas[0],bins=10)
ax[0,0].set_title(labels[0])
ax[0,1].hist(listas[1],bins=20)
ax[0,1].set_title(labels[1])
ax[1,0].hist(listas[2],bins=20)
ax[1,0].set_title(labels[2])
ax[1,1].hist(listas[3],bins=20)
ax[1,1].set_title(labels[3])
ax[2,0].hist(listas[4],bins=20)
ax[2,0].set_title(labels[4])
ax[2,1].hist(listas[5],bins=10)
ax[2,1].set_title(labels[5])
ax[0,0].set(xlabel='Tempo(s)',ylabel='Quantidade')
ax[0,1].set(xlabel='Tempo(s)',ylabel='Quantidade')
ax[1,0].set(xlabel='Tempo(s)',ylabel='Quantidade')
ax[1,1].set(xlabel='Tempo(s)',ylabel='Quantidade')
ax[2,0].set(xlabel='Tempo(s)',ylabel='Quantidade')
ax[2,1].set(xlabel='Tempo(s)',ylabel='Quantidade')
fig.tight_layout()
plt.show()

fig,ax = plt.subplots()
x = np.arange(len(labels))
width = 0.35
rec1 = ax.bar(x-width/2,max_values,width,label='High Water Mark')
rec2 = ax.bar(x+width/2,medias,width,label='Médias')
ax.bar_label(rec1,fmt='%.4f')
ax.bar_label(rec2,fmt='%.4f')
ax.set_ylabel('Tempo(s)')
ax.set_xticks(x,labels)
ax.legend()

fig.tight_layout()
plt.show()