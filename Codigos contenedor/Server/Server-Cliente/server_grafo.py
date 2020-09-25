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
 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

UDPServerSocket2.bind((localIP, 20002))
 
UDPServerSocket3.bind((localIP, 20003))


UDPServerSocket4.bind((localIP, 20004))
 
UDPServerSocket5.bind((localIP, 20005))

 
UDPServerSocket6.bind((localIP, 20006))


UDPServerSocket7.bind((localIP, 20007))
 
UDPServerSocket8.bind((localIP, 20008))
print("UDP server up and listening")

# Grafica 
fig, ax=plt.subplots(3,1,constrained_layout=True)
#fig1, ax1=plt.subplots(2,1,constrained_layout=True) #accion de control
x1=[]
x2=[]
x3=[] 
u1=[]
u2=[]
q1=[]
q2=[]
t=[]
global message
message=0

def animate(i):
    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    x1.append(float(message))
    
    bytesAddressPair = UDPServerSocket8.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    t.append(float(message))
    
    
    bytesAddressPair = UDPServerSocket4.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    q1.append(float(message))
    
    bytesAddressPair = UDPServerSocket5.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    
    q2.append(float(message))
    
    
    ax[0].clear()
    ax[0].plot(t,x1,'r',t,q1,'--b')
    ax[0].set_title('Nivel del fluido tanque 1')
    ax[0].set_xlabel('Tiempo(s)')
    ax[0].set_ylabel('Nivel(m)')
    
    
    
    
    bytesAddressPair = UDPServerSocket2.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    x2.append(float(message))
    ax[1].clear()
    ax[1].plot(t,x2,'b',t,q2,'--r')
    ax[1].set_title('Nivel del fluido tanque 2')
    ax[1].set_xlabel('Tiempo(s)')
    ax[1].set_ylabel('Nivel(m)')


    
    bytesAddressPair = UDPServerSocket3.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    
    x3.append(float(message))
    ax[2].clear()
    ax[2].plot(t,x3,'k')
    ax[2].set_title('Nivel del fluido tanque 3')
    ax[2].set_xlabel('Tiempo(s)')
    ax[2].set_ylabel('Nivel(m)')
    
   
    

ani=animation.FuncAnimation(fig,animate,interval=50)
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
