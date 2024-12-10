#!/usr/bin/env python3
import subprocess
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Maintainer(Node):

    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("node: %s started" % name)
        self.command_subscribe_break_ = self.create_subscription(Int32, "command_break", self.command_callback_break, 10)
        #########################################################################
        # if compile is needed, it has to be done in advance, for example: here #
        #########################################################################
    
    def command_callback_break(self, msg):
        if msg.data == 999:
            time.sleep(1) # make sure payload03old is killed
            # also, just a demo. However, multprocess is avilable through python
            subprocess.run("ros2 param set /payload01 use_new 1 && ros2 run maintaince_pkg payload03", shell=True)


def main(args=None):
    rclpy.init(args=args)
    node = Maintainer("maintainer")
    rclpy.spin(node)
    rclpy.shutdown()