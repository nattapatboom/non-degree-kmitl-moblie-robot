#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def main ():
    rospy.init_node('tutlebot_control', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    velocity_msg = Twist()
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        velocity_msg.linear.x = 0.2
        velocity_msg.angular.z = 0.0
        pub.publish(velocity_msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        main ()
    except rospy.ROSInterruptException:
        pass
