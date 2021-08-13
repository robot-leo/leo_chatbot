#!/usr/bin/env python
# coding: utf-8

import rospy
import actionlib
import sys

from speak_out_loud.msg import SpeakGoal, Priority
from std_msgs.msg import String

class Client(object) :
	def __init__(self):
		rospy.logwarn("AIML client is started")
		self.goal = SpeakGoal()
		# self.goal.sender_node = rospy.get_name()
		self.goal.priority = Priority.MESSAGE
		# self.load_params()
		self._pub = rospy.Publisher("/speak_out_loud_texts", SpeakGoal, queue_size=1)
		rospy.Subscriber("/respon", String, self.resp_cb)
		rospy.on_shutdown(self.shutdown)

	def resp_cb(self, data):
		response = data.data
		rospy.loginfo("Response ::%s",response)
		self.goal.text = response
		self._pub.publish(self.goal)

	def run(self):
		rospy.spin()

	def shutdown(self):
		rospy.logwarn("AIML Client node is closed")

if __name__ == '__main__':
	try:
		rospy.init_node('aiml_soundplay_client')
		rospy.logwarn('Press Ctrl+C to shutdown node')
		client = Client()
		client.run()

	except rospy.ROSInterruptException:
		pass