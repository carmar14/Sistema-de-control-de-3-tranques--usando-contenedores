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
        #plt.figure()







def main(args=None):
    plt.plot([1, 2, 3],[2, 4, 5])
    plt.show()
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
