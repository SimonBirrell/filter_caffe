#!/usr/bin/env python

# filter_caffe
# ============
# Filters the output of ros_caffe (caffe_ret) aand republished only
# the best hits on a new topic (caffe_best).
#
# Written by Simon Birrell
# BSD License.

import sys
print
print sys.path
print

import rospy
from filter_caffe import filter_caffe_message
from std_msgs.msg import String

Pub = 0

def received_caffe_message(data):
    global Pub
    filtered_message = filter_caffe_message(data)
    if filtered_message:
        Pub.publish(filtered_message)
        rospy.loginfo(filtered_message)
    else:
        rospy.loginfo("No good hit.")            

def filter_caffe_node():
    global Pub 
    Pub = rospy.Publisher('caffe_best', String, queue_size=10)
    rospy.init_node('filter_caffe', anonymous=True)
    rospy.Subscriber("caffe_ret", String, received_caffe_message)
    rospy.spin()

if __name__ == '__main__':
    try:
    	filter_caffe_message("")
        filter_caffe_node()
    except rospy.ROSInterruptException:
        pass

