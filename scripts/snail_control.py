#!/usr/bin/env python

# ROS Subscriber Node listener.py from:
#    https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#

import rospy

from hook.msg import Handset

SNAIL_STATES = ['IDLE',
                'CALLING_COUNSELOR',
                'IN_CALL']

snail_state = 'IDLE'

def handset_state_changed(data):
    global snail_state
    rospy.loginfo("Handset Picked-Up: %s", data.picked_up)

    if data.picked_up: # Handset picked up
        snail_state = 'CALLING_COUNSELOR'

    if not data.picked_up: # Handset hung-up
        snail_state = 'IDLE'

    rospy.loginfo("Snail State: %s", snail_state)

def snail_control():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('snail_control', anonymous=True)

    # Set-up Subscriptions
    rospy.Subscriber("hook", Handset, handset_state_changed)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        snail_control()
    except rospy.ROSInterruptException:
        pass
