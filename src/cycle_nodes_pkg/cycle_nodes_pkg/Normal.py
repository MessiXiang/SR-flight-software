#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Normal(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("Node:%s started!" % name)

def main(args=None):
    rclpy.init(args=args)
    node = Normal("normal")
    rclpy.spin(node)
    rclpy.shutdown()