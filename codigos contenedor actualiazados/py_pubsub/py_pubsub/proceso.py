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


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Proceso,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        u1=float(msg.u1)/10000.0
        u2=float(msg.u2)/10000.0
        t=float(msg.num)
        q1=float(msg.x1)/1000.0
        q2=float(msg.x2)/1000.0


        self.get_logger().info('u1: "%3.4f"' % u1)

        self.get_logger().info('u2: "%3.4f"' % u2)

        self.get_logger().info('tiempo: "%3.4f"' % t)

        self.get_logger().info('q1: "%3.4f"' % q1)

        self.get_logger().info('q2: "%3.4f"' % q2)

        bytesToSend=str.encode(str(u1))

        serverAddressPort=("10.90.135.1", 20006)

        bufferSize=1024

        udpcliente=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente.sendto(bytesToSend,serverAddressPort)

        bytesToSend2=str.encode(str(u2))

        serverAddressPort=("10.90.135.1", 20007)

        bufferSize=1024

        udpcliente2=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente2.sendto(bytesToSend2,serverAddressPort)

        bytesToSend3=str.encode(str(t))

        serverAddressPort=("10.90.135.1", 20008)

        bufferSize=1024

        udpcliente3=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente3.sendto(bytesToSend3,serverAddressPort)

        bytesToSend4=str.encode(str(q1))

        serverAddressPort=("10.90.135.1", 20004)

        bufferSize=1024

        udpcliente4=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente4.sendto(bytesToSend4,serverAddressPort)

        bytesToSend5=str.encode(str(q2))

        serverAddressPort=("10.90.135.1", 20005)

        bufferSize=1024

        udpcliente5=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente5.sendto(bytesToSend5,serverAddressPort)




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
