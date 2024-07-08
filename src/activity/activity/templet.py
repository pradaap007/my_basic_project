#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
class mycustomnode(Node):
   def __init__(self):
     super().__init__("node name")


def main(args=None):
    rclpy.init(args=args)
    node=mycustomnode
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
  main()