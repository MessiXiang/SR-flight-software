#!/usr/bin/env python3
import hashlib
import subprocess
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from more_interfaces.srv import Md5ver


class Payload01(Node):
    
    def __init__(self,name):
        super().__init__(name)
        self.no_response_count = 0
        self.verify_origin = 0
        self.max_timeout = 1.5
        self.restart_count_max = 3
        self.get_logger().info("Node:%s started" % name)

        self.command_subscribe_ = self.create_subscription(Int32, "command", self.command_callback, 10)
        self.command_subscribe2_ = self.create_subscription(Int32, "destroy", self.command_destroy, 10)

        self.add_server_ = self.create_service(Md5ver, "md5ver_srv12", self.hash_calc_md5)
        self.client_ = self.create_client(Md5ver, "md5ver_srv31")

    def command_callback(self, msg):
        if msg.data == 1:
            self.get_logger().info(f'received [{msg.data}]command')
            ##########################
            # some mission code here #
            ##########################
            # send your data via msg #
            ##########################
            self.get_logger().info(f'waiting for previous node\'s hashstr')
            self.send_request()

    def send_request(self):
        if rclpy.ok() and self.client_.wait_for_service(self.max_timeout) == False:
            self.get_logger().info(f"no response from previous node")
            self.no_response_count += 1
            
            if self.no_response_count >= self.restart_count_max:
                # Just a example with subprocess. Multiprocess version is under constraction.
                # Launch file is also acceptable
                subprocess.Popen("ros2 run restart_node_pkg payload03", shell=True)
                self.no_response_count = 0
            return
        
        request = Md5ver.Request()
        self.verify_origin = str(time.time())
        request.origin = self.verify_origin
        self.client_.call_async(request).add_done_callback(self.result_callback_)

    def result_callback_(self, result_future):
        response = result_future.result()
        self.get_logger().info(f"receive response: {response.md5sum}")
        expect_md5 = hashlib.md5(self.verify_origin.encode('utf-8')).hexdigest()
        
        if response.md5sum == expect_md5:
            self.get_logger().info(f"verify success!")
        else:
            self.get_logger().info(f"previous node isn\'t working correctly")
            self.no_response_count += 1
        
    def hash_calc_md5(self, request, response):
        response.md5sum = hashlib.md5(str(request.origin).encode('utf-8')).hexdigest()
        return response
    
    def command_destroy(self, msg):
        if msg.data == 1:
            self.get_logger().info(f'start self-destroy')
            self.destroy_service(self.add_server_)
            rclpy.shutdown()
            


def main(args=None):
    rclpy.init(args=args)
    node = Payload01("payload01")
    rclpy.spin(node)
    rclpy.shutdown()