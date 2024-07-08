#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusPublisher(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher")
        self.hwdsts_publisher = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.create_timer(1.0, self.hw_sts)
        self.get_logger().info("Hardware status publisher is ready")

    def hw_sts(self):
        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_ready = True
        msg.debug_message = "No debug messages"
        self.hwdsts_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
