# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import socket
import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node

#from std_msgs.msg import String
from tutorial_interfaces.msg import Control        # CHANGE
from tutorial_interfaces.msg import Proceso        # CHANGE
from tutorial_interfaces.msg import UIO1        # CHANGE

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            UIO1,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        x1u1=float(msg.x1u1)/10000.0
        x2u1=float(msg.x2u1)/10000.0
        x3u1=float(msg.x3u1)/10000.0
        x1u2=float(msg.x1u2)/10000.0
        x2u2=float(msg.x2u2)/10000.0
        x3u2=float(msg.x3u2)/10000.0
        x1l=float(msg.x1l)/10000.0
        x2l=float(msg.x2l)/10000.0
        x3l=float(msg.x3l)/10000.0
        ad=msg.ad
        ai1=msg.ai1
        ai2=msg.ai2
        v1=float(msg.v1)/10000.0
        v2=float(msg.v2)/10000.0

        '''
        self.get_logger().info('u1: "%3.4f"' % u1)

        self.get_logger().info('u2: "%3.4f"' % u2)

        self.get_logger().info('tiempo: "%3.4f"' % t)

        self.get_logger().info('q1: "%3.4f"' % q1)

        self.get_logger().info('q2: "%3.4f"' % q2)'''

        bytesToSend=str.encode(str(x1l))

        serverAddressPort=("10.90.135.1", 20009)

        bufferSize=1024

        udpcliente=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente.sendto(bytesToSend,serverAddressPort)

        bytesToSend2=str.encode(str(x2l))

        serverAddressPort=("10.90.135.1", 20010)

        bufferSize=1024

        udpcliente2=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente2.sendto(bytesToSend2,serverAddressPort)

        bytesToSend3=str.encode(str(x3l))

        serverAddressPort=("10.90.135.1", 20011)

        bufferSize=1024

        udpcliente3=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente3.sendto(bytesToSend3,serverAddressPort)

        bytesToSend4=str.encode(str(x1u1))

        serverAddressPort=("10.90.135.1", 20012)

        bufferSize=1024

        udpcliente4=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente4.sendto(bytesToSend4,serverAddressPort)

        bytesToSend5=str.encode(str(x2u1))

        serverAddressPort=("10.90.135.1", 20013)

        bufferSize=1024

        udpcliente5=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente5.sendto(bytesToSend5,serverAddressPort)
        
        bytesToSend6=str.encode(str(x3u1))

        serverAddressPort=("10.90.135.1", 20014)

        bufferSize=1024

        udpcliente6=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente6.sendto(bytesToSend6,serverAddressPort)

        bytesToSend7=str.encode(str(x1u2))

        serverAddressPort=("10.90.135.1", 20015)

        bufferSize=1024

        udpcliente7=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente7.sendto(bytesToSend7,serverAddressPort)

        bytesToSend8=str.encode(str(x2u2))

        serverAddressPort=("10.90.135.1", 20016)

        bufferSize=1024

        udpcliente8=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente8.sendto(bytesToSend8,serverAddressPort)

        bytesToSend9=str.encode(str(x3u2))

        serverAddressPort=("10.90.135.1", 20017)

        bufferSize=1024

        udpcliente9=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente9.sendto(bytesToSend9,serverAddressPort)

        bytesToSend10=str.encode(str(ad))

        serverAddressPort=("10.90.135.1", 20018)

        bufferSize=1024

        udpcliente10=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente10.sendto(bytesToSend10,serverAddressPort)
        
        bytesToSend11=str.encode(str(ai1))

        serverAddressPort=("10.90.135.1", 20019)

        bufferSize=1024

        udpcliente11=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente11.sendto(bytesToSend11,serverAddressPort)


        bytesToSend12=str.encode(str(ai2))

        serverAddressPort=("10.90.135.1", 20020)

        bufferSize=1024

        udpcliente12=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente12.sendto(bytesToSend12,serverAddressPort)
        
        bytesToSend13=str.encode(str(v1))

        serverAddressPort=("10.90.135.1", 20021)

        bufferSize=1024

        udpcliente13=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente13.sendto(bytesToSend13,serverAddressPort)

        bytesToSend14=str.encode(str(v2))

        serverAddressPort=("10.90.135.1", 20022)

        bufferSize=1024

        udpcliente14=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente14.sendto(bytesToSend14,serverAddressPort)




def main(args=None):
    
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
