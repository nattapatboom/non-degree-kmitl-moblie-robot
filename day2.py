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
    global current_pose
    current_pose = data


def main():
    global current_pose

    rospy.init_node('turtle_control', anonymous=True)
    rate = rospy.Rate(10)  # Hz

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, poseCallback)

    stage = 0  # 0 = Rotage , 1 move forward
    # Goal x = 7, y = 7

    while not rospy.is_shutdown():
        if stage == 0:
            d_x = 7.0 - current_pose.x
            d_y = 7.0 - current_pose.y
            th = math.atan2(d_y, d_x)

            if(current_pose.theta <= -3.14):
                current_pose.theta = abs(current_pose.theta)
            d_th = th - current_pose.theta
            vel.angular.z = d_th * 0.1
            #print(current_pose, vel.angular.z)

            if(abs(d_th) <= 0.01):
                print('Change State 1')
                stage = 1
        elif stage == 1:
            vel.linear.x = 0.1
            d_x = abs(7.0 - current_pose.x)
            d_y = abs(7.0 - current_pose.y)
            if ((d_x < 0.1) and (d_y < 0.1)):
                print('Change State 2')
                stage = 2
        else:
            print('Stop')
            vel.linear.x = 0
            vel.angular.z = 0
        pub.publish(vel)

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
