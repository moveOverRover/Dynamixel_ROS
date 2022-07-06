#! /bin/python3
import rospy
import actionlib
from dynamixel_workbench_msgs.srv import DynamixelCommand, DynamixelCommandResponse
from dynamixel_as_adapter.msg import DynamixelTurnDegreeAction, DynamixelTurnDegreeActionResult, DynamixelTurnDegreeActionFeedback

class Dynamixel_action_server(object):

    def __init__(self):
        # creates the action server
        self._as = actionlib.SimpleActionServer("dynamixel_action_server", DynamixelTurnDegreeAction, self.goal_callback, False)
        self.srv = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        self.Dynamixel_id = 1
        self._as.start()
        print('started_server')

    def int_map (self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def goal_callback(self, goal):
        rospy.loginfo('Executing goal...')

        feedback_msg = DynamixelTurnDegreeActionFeedback()
        result = DynamixelTurnDegreeActionResult()
        result.result = False
        
        if not(goal.goal >= -180 and goal.goal <= 180):
            feedback_msg.feedback = "goal of: " + str(goal.goal) + " is not in range -180~180"
            self._as.publish_feedback(feedback_msg)
            self._as.set_aborted()
            return result

        command = self.int_map(goal.goal, -180 , 180, 0, 4095)
        if self.srv('', self.Dynamixel_id, 'Goal_Position', command):
            result.result = True
            feedback_msg.feedback = "sucess, reached goal position: " + str(command)
        else:
            feedback_msg.feedback = "unable to reach goal position:" + str(command)

        self._as.publish_feedback(feedback_msg)
        self._as.set_succeeded(result)
        return result

if __name__ == '__main__':
    rospy.init_node('dynamixel_action_server')
    Dynamixel_action_server()
    rospy.spin()