#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped

global current_pose
current_pose = Pose()


def callback(data):
    global current_pose
    current_pose  = data.pose.pose
    print(current_pose)

def main ():
    global current_pose
    rospy.init_node('tutlebot_control', anonymous=True)
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    goalpose_msg = PoseStamped()

    rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, callback)

    rate = rospy.Rate(10) # 10hz

    stage = 0

    while not rospy.is_shutdown():
        if stage == 0:
            goalpose_msg.header.stamp = rospy.Time.now()
            goalpose_msg.header.frame_id = "map"

            goalpose_msg.pose.position.x = -1.00027115659
            goalpose_msg.pose.position.y = 0.564394023456
            goalpose_msg.pose.position.z = 0.0

            goalpose_msg.pose.orientation.x = 0.0
            goalpose_msg.pose.orientation.y = 0.0
            goalpose_msg.pose.orientation.z = -0.964123053304
            goalpose_msg.pose.orientation.w = 0.265455717752

            pub.publish(goalpose_msg)
            stage = 1
        if stage == 1:
            current_pose.position.x
            current_pose.position.y
            pass
        rate.sleep()

if __name__ == '__main__':
    try:
        main ()
    except rospy.ROSInterruptException:
        pass
