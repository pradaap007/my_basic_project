import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
class add_server_node(Node):
    def __init__(self):
        super().__init__("add_2_int_service_node")
        self.server_=self.create_service(AddTwoInts,"add_two_ints",self.add)
        self.get_logger().info("sever has been started")
    def add(self,request,response):
        response.sum=request.a + request.b

        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
        return response
def main(args=None):
    rclpy.init(args=args)
    node=add_server_node()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()