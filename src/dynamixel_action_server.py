#! /bin/python3
import rospy
import actionlib
from dynamixel_sdk_examples.msg import SetPosition
from dynamixel_as.msg import DynamixelTurnDegreeAction, DynamixelTurnDegreeActionResult, DynamixelTurnDegreeActionFeedback


class Dynamixel_action_server(object):

    def __init__(self):
        # creates the action server
        self._as = actionlib.SimpleActionServer("dynamixel_action_server", DynamixelTurnDegreeAction, self.goal_callback, False)
        self.publisher_ = rospy.Publisher("set_position", SetPosition, queue_size=10 )
        self.cmd = SetPosition()
        self.cmd.id = 1
        self._as.start()
        print('started_server')

    def int_map (self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def goal_callback(self, goal):
        print('Executing goal...')
        feedback_msg = DynamixelTurnDegreeActionFeedback()
        # goal.DynamixelTurnDegreeAction.succeed()
        result = DynamixelTurnDegreeActionResult()

        degrees = self.int_map(goal.goal, 0 , 360, 0, 4095)
        print(degrees)
        self.cmd.position = degrees
        self.publisher_.publish(self.cmd)

        feedback_msg.feedback = "Finished action server."
        self._as.publish_feedback(feedback_msg)
        result.result = True
        self._as.set_succeeded(result)
        return result

if __name__ == '__main__':
    rospy.init_node('dynamixel_action_server')
    Dynamixel_action_server()
    rospy.spin()