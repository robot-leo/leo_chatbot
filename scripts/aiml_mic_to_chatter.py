
# coding=utf-8			# -*- coding: utf-8 -*-
#!/usr/bin/env python


import rospy
import actionlib
import sys
import speech_recognition as SR


from actionlib_msgs.msg import GoalStatus, GoalStatusArray
from speech_recognition_msgs.msg import SpeechRecognitionCandidates
from std_msgs.msg import String
from urllib import unquote

class Client(object) :
	def __init__(self):
		rospy.logwarn("mic_to_aiml client is started")
		self._pub=rospy.Publisher("/chatter", String, queue_size=1)
		rospy.Subscriber("/speech_to_text", SpeechRecognitionCandidates, self.chat_cb)
		rospy.on_shutdown(self.shutdown)
		

	def chat_cb(self, transcript):
		rospy.loginfo("I Said ::%s", transcript.transcript)

		if len(transcript.transcript) > 0:
			word = transcript.transcript[0]
			rospy.loginfo(word)
			self._pub.publish(word)
		else: rospy.loginfo('ту мач вордс')
#		transcript = transcript.transcript[0]
#	self._pub.publish(transcript)


	def run(self):
		rospy.spin()

	def shutdown(self):
		rospy.logwarn("mic_to_aiml Client node is closed")

if __name__ == '__main__':
	try:
		rospy.init_node('aiml_mic_to_chatter_convert')
		rospy.logwarn('Press Ctrl+C to shutdown node')
		client = Client()
		client.run()

	except rospy.ROSInterruptException:
		pass 
