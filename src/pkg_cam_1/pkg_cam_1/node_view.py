# ros
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

# opencv2
import cv2
from cv_bridge import CvBridge


class NodeView(Node):
    def __init__(self):
        super().__init__('node_view')
        self.subscriber = self.create_subscription(
            msg_type = Image,
            topic='cam_image',
            callback=self.callback_1,
            qos_profile=10
        )
        self.bridge = CvBridge()


    def callback_1(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        cv2.imshow('Subscribe Image',cv_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()


def main():
    rclpy.init()
    node = NodeView()
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()