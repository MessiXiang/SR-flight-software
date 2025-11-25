#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Switcher(Node):

    def __init__(self,name):
        self.cycle_count = 1
        super().__init__(name)
        self.get_logger().info("node: %s started" % name)
        self.command_publisher_ = self.create_publisher(Int32, "command", 10)
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.cycle_count
        self.command_publisher_.publish(msg)
        self.get_logger().info(f'published: {msg.data}')
        self.cycle_count += 1
        if self.cycle_count > 3:
            self.cycle_count = 1

def main(args=None):
    rclpy.init(args=args)
    node = Switcher("switcher")
    rclpy.spin(node)
    rclpy.shutdown()