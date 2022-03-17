#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

def callback(msg):
    print msg.orientation.x
    print msg.orientation.y
    print msg.orientation.z
    print msg.orientation.w

rospy.init_node('get_imu_data')

sub = rospy.Subscriber('imu', Imu, callback)

rospy.spin()