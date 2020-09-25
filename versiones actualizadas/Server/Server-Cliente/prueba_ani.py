import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools
 

# Grafica 
fig, ax=plt.subplots(3,3,constrained_layout=True)
#fig1, ax1=plt.subplots(3,1,constrained_layout=True)
#fig2, ax2=plt.subplots(3,1,constrained_layout=True)
#fig1, ax1=plt.subplots(2,1,constrained_layout=True) #accion de control
t=[]
x1=[]

x2=[]
x3=[] 
u1=[]
u2=[]
q1=[]
q2=[]
x4=[]
x5=[]
x6=[]
x7=[]
x8=[]
x9=[] 
x1u1=[]
x2u1=[]
x3u1=[] 
x1u2=[]
x2u2=[]
x3u2=[] 
ad=[]
ai1=[]
ai2=[]
v1=[]
v2=[]

global message
message=0

def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
        
        
def tanque1(i):
    
    
    
    
    x1.append(i*i)
    t.append(i)
    
    ax[0,0].clear()
    ax[0,0].plot(t,x1,'k')#,t,q1,'--r',t,x1l,'b')
    ax[0,0].set_title('Nivel del fluido tanque 1')
    ax[0,0].set_xlabel('Tiempo(s)')
    ax[0,0].set_ylabel('Nivel(m)')
    
    
    x2.append(i*i*i-2500*i+89)
    #t.append(i)
    
    ax[0,1].clear()
    ax[0,1].plot(t,x2,'k')#,t,q1,'--r',t,x1l,'b')
    ax[0,1].set_title('Nivel del fluido tanque 1')
    ax[0,1].set_xlabel('Tiempo(s)')
    ax[0,1].set_ylabel('Nivel(m)')
    
    x3.append(i*i*i-2500*i+890)
    #t.append(i)
    
    ax[0,2].clear()
    ax[0,2].plot(t,x3,'k')#,t,q1,'--r',t,x1l,'b')
    ax[0,2].set_title('Nivel del fluido tanque 1')
    ax[0,2].set_xlabel('Tiempo(s)')
    ax[0,2].set_ylabel('Nivel(m)')
    
    x4.append(-i*i*i+250*i+89)
    
    ax[1,0].clear()
    ax[1,0].plot(t,x4,'k')#,t,q1,'--r',t,x1l,'b')
    ax[1,0].set_title('Nivel del fluido tanque 1')
    ax[1,0].set_xlabel('Tiempo(s)')
    ax[1,0].set_ylabel('Nivel(m)')
    
    
    x5.append(-i*i-250*i+89)
    #t.append(i)
    
    ax[1,1].clear()
    ax[1,1].plot(t,x5,'k')#,t,q1,'--r',t,x1l,'b')
    ax[1,1].set_title('Nivel del fluido tanque 1')
    ax[1,1].set_xlabel('Tiempo(s)')
    ax[1,1].set_ylabel('Nivel(m)')
    
    x6.append(-6*i+890)
    #t.append(i)
    
    ax[1,2].clear()
    ax[1,2].plot(t,x6,'k')#,t,q1,'--r',t,x1l,'b')
    ax[1,2].set_title('Nivel del fluido tanque 1')
    ax[1,2].set_xlabel('Tiempo(s)')
    ax[1,2].set_ylabel('Nivel(m)')
    
    x7.append(-i*i+250*i+89)
    
    ax[2,0].clear()
    ax[2,0].plot(t,x7,'k')#,t,q1,'--r',t,x1l,'b')
    ax[2,0].set_title('Nivel del fluido tanque 1')
    ax[2,0].set_xlabel('Tiempo(s)')
    ax[2,0].set_ylabel('Nivel(m)')
    
    
    x8.append(i*i-250*i+89)
    #t.append(i)
    
    ax[2,1].clear()
    ax[2,1].plot(t,x8,'k')#,t,q1,'--r',t,x1l,'b')
    ax[2,1].set_title('Nivel del fluido tanque 1')
    ax[2,1].set_xlabel('Tiempo(s)')
    ax[2,1].set_ylabel('Nivel(m)')
    
    x9.append(6*i+890)
    #t.append(i)
    
    ax[2,2].clear()
    ax[2,2].plot(t,x9,'k')#,t,q1,'--r',t,x1l,'b')
    ax[2,2].set_title('Nivel del fluido tanque 1')
    ax[2,2].set_xlabel('Tiempo(s)')
    ax[2,2].set_ylabel('Nivel(m)')
    
    
    '''
    ax[1].clear()
    ax[1].plot(t,x1,'k',t,x1u1,'r')
    ax[1].set_title('Nivel del fluido tanque 1')
    ax[1].set_xlabel('Tiempo(s)')
    ax[1].set_ylabel('Nivel(m)')
    
    ax[2].clear()
    ax[2].plot(t,x1,'k',t,x1u2,'r')
    ax[2].set_title('Nivel del fluido tanque 1')
    ax[2].set_xlabel('Tiempo(s)')
    ax[2].set_ylabel('Nivel(m)')'''
    
    
    
    '''
    bytesAddressPair = UDPServerSocket2.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    x2.append(float(message))
    
    bytesAddressPair = UDPServerSocket10.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x2l.append(float(message))
    
    bytesAddressPair = UDPServerSocket13.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x2u1.append(float(message))
    
    bytesAddressPair = UDPServerSocket16.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x2u2.append(float(message))
    
    ax1[0].clear()
    ax1[0].plot(t,x2,'k',t,q2,'--r',t,x2l,'b')
    ax1[0].set_title('Nivel del fluido tanque 2')
    ax1[0].set_xlabel('Tiempo(s)')
    ax1[0].set_ylabel('Nivel(m)')
    
    ax1[1].clear()
    ax1[1].plot(t,x2,'k',t,x2u1,'r')
    ax1[1].set_title('Nivel del fluido tanque 2')
    ax1[1].set_xlabel('Tiempo(s)')
    ax1[1].set_ylabel('Nivel(m)')
    
    ax1[2].clear()
    ax1[2].plot(t,x2,'k',t,x2u2,'r')
    ax1[2].set_title('Nivel del fluido tanque 2')
    ax1[2].set_xlabel('Tiempo(s)')
    ax1[2].set_ylabel('Nivel(m)')


    
    bytesAddressPair = UDPServerSocket3.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    x3.append(float(message))
    
    bytesAddressPair = UDPServerSocket11.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x3l.append(float(message))
    
    bytesAddressPair = UDPServerSocket14.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x3u1.append(float(message))
    
    bytesAddressPair = UDPServerSocket17.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x3u2.append(float(message))
    
    ax2[0].clear()
    ax2[0].plot(t,x3,'k',t,x3l,'r')
    ax2[0].set_title('Nivel del fluido tanque 3')
    ax2[0].set_xlabel('Tiempo(s)')
    ax2[0].set_ylabel('Nivel(m)')
    
    ax2[1].clear()
    ax2[1].plot(t,x3,'k',t,x3u2,'r')
    ax2[1].set_title('Nivel del fluido tanque 3')
    ax2[1].set_xlabel('Tiempo(s)')
    ax2[1].set_ylabel('Nivel(m)')
    
    ax2[1].clear()
    ax2[1].plot(t,x3,'k',t,x3u1,'r')
    ax2[1].set_title('Nivel del fluido tanque 3')
    ax2[1].set_xlabel('Tiempo(s)')
    ax2[1].set_ylabel('Nivel(m)')'''
    

    
   
    
ani=animation.TimedAnimation(fig,interval=100)
#ani=animation.FuncAnimation(fig,tanque1,frames=100,interval=500)
#ani2=animation.FuncAnimation(fig1,tanque2,interval=51)
#ani3=animation.FuncAnimation(fig2,tanque3,interval=50)
plt.show()

# Listen for incoming datagrams


'''
while(True):
    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
    
    

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)
    
'''
