import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64



class number_pub(Node):
    def __init__(self):
        super().__init__("acty1")
        self.pub_n=self.create_publisher(Int64,"number",10)
        self.number=2
        self.get_logger().info("number pub started")
        self.tmr=self.create_timer(1.0,number_pub)
    def number_pub(self):
        msg=Int64()
        msg.data=self.number
        self.pub_n.publish(msg)


    
def main(args=None):
    rclpy.init(args=args)
    node=number_pub()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()