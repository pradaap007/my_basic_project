#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
class numbercounter(Node):
   def __init__(self):
     
     super().__init__("number_counter")
     self.count_=0
     self.pub=self.create_publisher(Int64,"number_counter",10)
     self.sub=self.create_subscription(Int64,"num_ct",self.callback,10)
     self.counter_ser=self.create_service(SetBool,"num",self.call_backcounter)
     self.get_logger().info("node starts")
   def callback(self,msg):
      self.count_+=msg.data
      new_msg=Int64()
      new_msg.data=self.count_
      self.pub.publish(new_msg)
   def call_backcounter(self,request,response):
      if request.data:
         self.count_=0
         response.success=True
         response.message="counter has beenm rested"
      else:
         response.success=False
         response.message="counter doesnt reseted"
      return response
      


def main(args=None):
    rclpy.init(args=args)
    node=numbercounter()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
  main()