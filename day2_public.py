#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('turtle_control', anonymous=True)
    rate = rospy.Rate(10)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = 1.0
        vel.angular.z = 1.0

        pub.publish(vel)

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
