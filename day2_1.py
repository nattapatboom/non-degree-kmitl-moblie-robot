#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import math

vel = Twist()
current_pose = Pose()

def poseCallback(data):
    print(data)
    current_pose = data


def main():
    rospy.init_node('turtle_control', anonymous=True)
    rate = rospy.Rate(10)  # Hz

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, poseCallback)

    timestart = time.time()

    while not rospy.is_shutdown():
        timenow = time.time()
        current = timenow - timestart
        if(0 < current < 2):
            vel.linear.x = 1.0
            vel.angular.z = 0.0
        elif(2 <= current < 5):
            vel.linear.x = 0.0
            vel.angular.z = 1.0
        else:
            vel.linear.x = 0.0
            vel.angular.z = 0.0
        pub.publish(vel)

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
