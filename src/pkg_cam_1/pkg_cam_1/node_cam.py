#ros2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

# opencv2
import cv2
from cv_bridge import CvBridge




class NodeCam(Node):
    def __init__(self):
        super().__init__('node_cam')
        self.publisher = self.create_publisher(
            msg_type=Image,
            topic='cam_image',
            qos_profile=10
        )
        self.cap = cv2.VideoCapture(2)
        self.bridge = CvBridge()
        self.timer = self.create_timer(
            timer_period_sec=0.01,
            callback=self.publish_
        )

    def publish_(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.publisher.publish( msg )

def main():
    rclpy.init()
    node = NodeCam()
    rclpy.spin(node)



if __name__=="__main__":
    main()