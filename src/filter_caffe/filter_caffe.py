#!/usr/bin/env python

# filter_caffe
# ============
# Filters the output of ros_caffe (caffe_ret) aand republished only
# the best hits on a new topic (caffe_best).
#
# Written by Simon Birrell
# BSD License.

import rospy

# Lowest probability at which we pass on the best match
# Otherwise considered to be no match
#
PROBABILITY_THRESHOLD = 0.5

# Examples of caffe_message 
#
# [0.832006 - n04554684 washer, automatic washer, washing machine]
# [0.0191289 - n03691459 loudspeaker, speaker, speaker unit, loudspeaker system, speaker system]
# [0.0161815 - n03976467 Polaroid camera, Polaroid Land camera]
# [0.0135932 - n04447861 toilet seat]
# [0.0115129 - n04125021 safe]
#
def filter_caffe_message(caffe_message):
    lines = str(caffe_message).splitlines()
    if (len(lines) == 0):
        return None
    first_line = lines[0]
    tokens = first_line.split(" ")
    if (len(tokens)<2):
        return None
    raw_probability = tokens[1].split("[")   
    if (len(raw_probability)<2):
        return None
    probability = float(raw_probability[1])
    if (probability>PROBABILITY_THRESHOLD):
        object_list = first_line.split(" - ")[1][10:]
        first_object = object_list.split(",")[0]
        return first_object
    return None

if __name__ == '__main__':
    try:
        filter_caffe_node()
    except rospy.ROSInterruptException:
        pass

