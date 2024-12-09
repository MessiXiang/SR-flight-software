#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String

class Payload03(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("Node:%s started!" % name)

        self.command_subscribe_ = self.create_subscription(Int32, "command", self.command_callback, 10)
        self.command_publisher_ = self.create_publisher(String, "data_payload03", 10)

    def command_callback(self, msg):
        if msg.data == 3:
            self.get_logger().info(f'received [{msg.data}] command, start mission')
            ##########################
            # some mission code here #
            ##########################
            # send your data via msg #
            ##########################

def main(args=None):
    rclpy.init(args=args)
    node = Payload03("payload03")
    rclpy.spin(node)
    rclpy.shutdown()