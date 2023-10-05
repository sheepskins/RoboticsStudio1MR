#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

seq = 0

if __name__ == "__main__":
    rospy.init_node("Path_Planner")
    rospy.loginfo("Starting Path Planner")
    
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    
    while not rospy.is_shutdown():
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        seq += 1
        goal.target_pose.header.stamp = rospy.Time.now()

        pos = input("Input Pose as X,Y,Z,x,y,z,w: ")
        pos = pos.split(',')

        goal.target_pose.pose.position.x = (float(pos[0]))
        goal.target_pose.pose.position.y = (float(pos[1]))
        goal.target_pose.pose.position.z = (float(pos[2]))
        goal.target_pose.pose.orientation.x = (float(pos[3]))
        goal.target_pose.pose.orientation.y = (float(pos[4]))
        goal.target_pose.pose.orientation.z = (float(pos[5]))
        goal.target_pose.pose.orientation.w = (float(pos[6]))
        
        client.send_goal(goal)
        client.wait_for_result()
