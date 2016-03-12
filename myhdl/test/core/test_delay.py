from __future__ import absolute_import
import warnings

from myhdl._compat import integer_types
from myhdl._delay import delay

class Testdelay(object):
	def cases(self):
		""" test cases for delay values """
		self.val = [-1,6,7,8]

	def testdelay(self):
		""" test for delay type and value """
		self.cases()
		for i in self.val:
			if not isinstance(i, integer_types) or i < 0:
					try:
						res = delay(i)
						raise AssertionError
					except TypeError:
						pass
			else:
				testdelayi = delay(i)
				assert testdelayi._time == i