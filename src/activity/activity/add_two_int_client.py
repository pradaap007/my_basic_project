#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial
class addtwointclient(Node):
   def __init__(self):
     super().__init__("add_two_int_oop")
     self.addtwoint_server(6,7)
     self.addtwoint_server(5,5)
   def addtwoint_server(self ,a ,b):
      client=self.create_client(AddTwoInts,"add_two_ints")
      while not client.wait_for_service(1.0):
         self.get_logger().warn("no response......")
      rqt=AddTwoInts.Request()
      rqt.a=a
      rqt.b=b
      future=client.call_async(rqt)
      future.add_done_callback(
         partial(self.callback_call_add_two_ints,a=a,b=b))
   def callback_call_add_two_ints(self, future,a,b):
       try:
        response= future.result()
        self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))
       except Exception as e:
        self.get_logger().error("sevice call failed %r"%(e,))
def main(args=None):
    rclpy.init(args=args)
    node=addtwointclient()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
  main()