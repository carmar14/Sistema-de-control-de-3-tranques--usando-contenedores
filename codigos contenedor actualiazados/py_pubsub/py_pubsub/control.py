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
            Control,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
       	x1=float(msg.x1)/10000.0
        x2=float(msg.x2)/10000.0
        x3=float(msg.x3)/10000.0


        self.get_logger().info('x1: "%3.4f"' % x1)

        self.get_logger().info('x2: "%3.4f"' % x2)

        self.get_logger().info('x3: "%3.4f"' % x3)

        #self.get_logger().info('q1: "%3.4f"' % q1)

        #self.get_logger().info('q2: "%3.4f"' % q2)

        bytesToSend=str.encode(str(x1))

        serverAddressPort=("10.90.135.1", 20001)

        bufferSize=1024

        udpcliente=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente.sendto(bytesToSend,serverAddressPort)

        bytesToSend2=str.encode(str(x2))

        serverAddressPort=("10.90.135.1", 20002)

        bufferSize=1024

        udpcliente2=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente2.sendto(bytesToSend2,serverAddressPort)

        bytesToSend3=str.encode(str(x3))

        serverAddressPort=("10.90.135.1", 20003)

        bufferSize=1024

        udpcliente3=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        udpcliente3.sendto(bytesToSend3,serverAddressPort)


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
