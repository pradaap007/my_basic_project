import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.msg import String




class number_sub(Node):
    def __init__(self):
        super().__init__("acty1_sub")
        self.counter=0
        self.ct_pub=self.create_publisher(String,"num_ct",10)
        self.num_sub=self.create_subscription(Int64,"num",self.cnum,10)
        self.get_logger().info("number sub satrted")
        self.tmr=self.create_timer(1.0,self.pub)
    def cnum(self,msg):
        self.counter+=msg.data
        self.get_logger().info(str(self.counter))        
    def pub(self):
        msg=String()
        msg.data="hello"
        self.ct_pub.publish(msg)

   
        

    
def main(args=None):
    rclpy.init(args=args)
    node=number_sub()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()