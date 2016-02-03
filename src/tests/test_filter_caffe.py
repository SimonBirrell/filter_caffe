# Tests for filter_caffe node
#

import nose
from filter_caffe.filter_caffe import filter_caffe_message

class TestFilterCaffe():

	def test_standard_message(self):
		input_message = """ [0.839569 - n04554684 washer, automatic washer, washing machine]
[0.0211603 - n03691459 loudspeaker, speaker, speaker unit, loudspeaker system, speaker system]
[0.012341 - n03976467 Polaroid camera, Polaroid Land camera]
[0.0117927 - n04447861 toilet seat]
[0.0110748 - n04125021 safe] """
		output_message = filter_caffe_message(input_message)
		nose.tools.eq_(output_message, "washer", "first name of first line selected")

	def test_low_probability(self):
		input_message = """ [0.139569 - n04554684 washer, automatic washer, washing machine]
[0.0211603 - n03691459 loudspeaker, speaker, speaker unit, loudspeaker system, speaker system]
[0.012341 - n03976467 Polaroid camera, Polaroid Land camera]
[0.0117927 - n04447861 toilet seat]
[0.0110748 - n04125021 safe] """
		output_message = filter_caffe_message(input_message)
		nose.tools.eq_(output_message, None, "low probability first line not selected")

	def test_empty(self):
		input_message = ""
		output_message = filter_caffe_message(input_message)
		nose.tools.eq_(output_message, None, "Empty input strig generates None")

