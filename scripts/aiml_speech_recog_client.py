#!/usr/bin/env python


import rospy
from std_msgs.msg import String


rospy.init_node('aiml_speech_recog_client')

pub = rospy.Publisher('/speak_out_loud_text', String,queue_size=1)
r = rospy.Rate(1) # 10hz

def get_speech(data):

	speech_text=data.data
	rospy.loginfo("I said:: %s",speech_text)
	pub.publish(speech_text)	


def listener():
	rospy.loginfo("Starting Speech Recognition")
	rospy.Subscriber("/respon", String, get_speech)
	rospy.spin()

while not rospy.is_shutdown():
	listener()

   
