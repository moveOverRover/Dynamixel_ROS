#! /bin/python3

import rospy
import actionlib
from dynamixel_as_adapter.msg import DynamixelTurnDegreeAction, DynamixelTurnDegreeActionGoal

def feedback_callback(feedback):
    print(feedback)

rospy.init_node('dynamixel_action_client_example')
client = actionlib.SimpleActionClient('/dynamixel_action_server', DynamixelTurnDegreeAction)
client.wait_for_server()
print("connected to server")

goal = DynamixelTurnDegreeActionGoal()
goal.goal = int(input("enter an integer -180~180\n"))
client.send_goal(goal, feedback_cb=feedback_callback)
client.wait_for_result()
    
print('[Result] State: %d'%(client.get_state()))