import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 

localIP     = "10.90.135.1"

localPort   = 20001

bufferSize  = 1024

 

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram sockets proceso

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket2 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket3 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Referencias
UDPServerSocket4 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket5 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Accciones de control
UDPServerSocket6 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


UDPServerSocket7 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Tiempo
UDPServerSocket8 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#OL
UDPServerSocket9 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket10 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket11 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#UIOs
UDPServerSocket12 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket13 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket14 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket15 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket16 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket17 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#alarmas
UDPServerSocket18 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket19 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket20 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket21 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket22 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

UDPServerSocket2.bind((localIP, 20002))
 
UDPServerSocket3.bind((localIP, 20003))


UDPServerSocket4.bind((localIP, 20004))
 
UDPServerSocket5.bind((localIP, 20005))

 
UDPServerSocket6.bind((localIP, 20006)) # accion u1


UDPServerSocket7.bind((localIP, 20007)) # accion u2
 
UDPServerSocket8.bind((localIP, 20008))
#OL
UDPServerSocket9.bind((localIP, 20009)) 

UDPServerSocket10.bind((localIP, 20010))
 
UDPServerSocket11.bind((localIP, 20011))

#UIOS
UDPServerSocket12.bind((localIP, 20012))
 
UDPServerSocket13.bind((localIP, 20013))

 
UDPServerSocket14.bind((localIP, 20014)) # accion u1


UDPServerSocket15.bind((localIP, 20015)) # accion u2
 
UDPServerSocket16.bind((localIP, 20016))


UDPServerSocket17.bind((localIP, 20017))
#ALARMAS 
UDPServerSocket18.bind((localIP, 20018))

 
UDPServerSocket19.bind((localIP, 20019)) # accion u1


UDPServerSocket20.bind((localIP, 20020)) # accion u2
 
UDPServerSocket21.bind((localIP, 20021))

UDPServerSocket22.bind((localIP, 20022))

print("UDP server up and listening")

# Grafica 
fig, ax=plt.subplots(3,4,constrained_layout=True)
#fig1, ax1=plt.subplots(3,1,constrained_layout=True)
#fig2, ax2=plt.subplots(3,1,constrained_layout=True)
#fig1, ax1=plt.subplots(2,1,constrained_layout=True) #accion de control
x1=[]
x2=[]
x3=[] 
u1=[]
u2=[]
q1=[]
q2=[]
t=[]
x1l=[]
x2l=[]
x3l=[] 
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

def tanque1(i):
    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x1.append(float(message))
    
    
    bytesAddressPair = UDPServerSocket9.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x1l.append(float(message))
    
    bytesAddressPair = UDPServerSocket12.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x1u1.append(float(message))
    
    bytesAddressPair = UDPServerSocket15.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x1u2.append(float(message))
    
    bytesAddressPair = UDPServerSocket8.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    
    t.append(float(message))
    
    
    bytesAddressPair = UDPServerSocket4.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    q1.append(float(message))
    
    bytesAddressPair = UDPServerSocket5.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    q2.append(float(message))
    
    
    ax[0,0].clear()
    ax[0,0].plot(t,x1,'k',t,q1,'--b',t,x1l,'r')
    ax[0,0].set_title('Nivel del fluido tanque 1')
    ax[0,0].set_xlabel('Tiempo(s)')
    ax[0,0].set_ylabel('Nivel(m)')
    
    ax[1,0].clear()
    ax[1,0].plot(t,x1,'k',t,x1u1,'r')
    ax[1,0].set_title('Nivel del fluido tanque 1')
    ax[1,0].set_xlabel('Tiempo(s)')
    ax[1,0].set_ylabel('Nivel(m)')
    
    ax[2,0].clear()
    ax[2,0].plot(t,x1,'k',t,x1u2,'r')
    ax[2,0].set_title('Nivel del fluido tanque 1')
    ax[2,0].set_xlabel('Tiempo(s)')
    ax[2,0].set_ylabel('Nivel(m)')
    
    
    
    
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
    
    ax[0,1].clear()
    ax[0,1].plot(t,x2,'k',t,q2,'--r',t,x2l,'b')
    ax[0,1].set_title('Nivel del fluido tanque 2')
    ax[0,1].set_xlabel('Tiempo(s)')
    ax[0,1].set_ylabel('Nivel(m)')
    
    ax[1,1].clear()
    ax[1,1].plot(t,x2,'k',t,x2u1,'r')
    ax[1,1].set_title('Nivel del fluido tanque 2')
    ax[1,1].set_xlabel('Tiempo(s)')
    ax[1,1].set_ylabel('Nivel(m)')
    
    ax[2,1].clear()
    ax[2,1].plot(t,x2,'k',t,x2u2,'r')
    ax[2,1].set_title('Nivel del fluido tanque 2')
    ax[2,1].set_xlabel('Tiempo(s)')
    ax[2,1].set_ylabel('Nivel(m)')


    
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
    
    ax[0,2].clear()
    ax[0,2].plot(t,x3,'k',t,x3l,'r')
    ax[0,2].set_title('Nivel del fluido tanque 3')
    ax[0,2].set_xlabel('Tiempo(s)')
    ax[0,2].set_ylabel('Nivel(m)')
    
    ax[1,2].clear()
    ax[1,2].plot(t,x3,'k',t,x3u2,'r')
    ax[1,2].set_title('Nivel del fluido tanque 3')
    ax[1,2].set_xlabel('Tiempo(s)')
    ax[1,2].set_ylabel('Nivel(m)')
    
    ax[2,2].clear()
    ax[2,2].plot(t,x3,'k',t,x3u1,'r')
    ax[2,2].set_title('Nivel del fluido tanque 3')
    ax[2,2].set_xlabel('Tiempo(s)')
    ax[2,2].set_ylabel('Nivel(m)')
    
    bytesAddressPair = UDPServerSocket18.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    ad.append(float(message))
    
    bytesAddressPair = UDPServerSocket19.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    ai1.append(float(message))
    
    bytesAddressPair = UDPServerSocket20.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    ai2.append(float(message))
    
    bytesAddressPair = UDPServerSocket21.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    v1.append(float(message))
    
    bytesAddressPair = UDPServerSocket22.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    v2.append(float(message))
    
    ax[0,3].clear()
    ax[0,3].plot(t,ad,'k',t,ai1,'--r',t,ai2,'ob')
    ax[0,3].set_title('Deteccion y aislamiento')
    ax[0,3].set_xlabel('Tiempo(s)')
    ax[0,3].set_ylabel('Alarma')
    
    ax[1,3].clear()
    ax[1,3].plot(t,v1,'k')
    ax[1,3].set_title('Ataque en 1')
    ax[1,3].set_xlabel('Tiempo(s)')
    ax[1,3].set_ylabel('Nivel(m)')
    
    ax[2,3].clear()
    ax[2,3].plot(t,v2,'k')
    ax[2,3].set_title('Ataque en 2')
    ax[2,3].set_xlabel('Tiempo(s)')
    ax[2,3].set_ylabel('Nivel(m)')

    

def tanque2(i):
    
    
    bytesAddressPair = UDPServerSocket5.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    q2.append(float(message))
    
    
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


    

def tanque3(i):
    
    
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
    ax2[1].set_ylabel('Nivel(m)') 
    
    
    
   
    

ani=animation.FuncAnimation(fig,tanque1,interval=600)
#ani2=animation.FuncAnimation(fig1,tanque2,interval=50)
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
