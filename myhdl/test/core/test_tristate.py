from __future__ import absolute_import
import warnings

from myhdl._Signal import _Signal, _DelayedSignal
from myhdl._simulator import _siglist

from myhdl._tristate import _DelayedTristate, _Tristate, _TristateDriver,Tristate

class TestTristate(object):
	def cases(self):

		""" Test cases for value and delay """
		self.val = [None,1,2,'0010']
		self.delay = [-1,0,None,5]

		""" Test cases for resolve function """

		lst1 = [None,None,None,None]
		lst2 = [None,2,None,None]
		lst3 = [None,1,None,2]
		lst4 = [1,None,None,None]
		self.Lst = [lst1,lst2,lst3,lst4]
		self.Lstout = [None,2,None,1]

   
	def testTristate(self):
		""" checks delay and decides to call Tristate """
		self.cases()
		for d,v in zip(self.delay,self.val):
			if d is not None:
				if d >= 0:
			                res = Tristate(v,d)
					assert isinstance(res,_DelayedTristate)
                                else:
					try:
			                        res = Tristate(v,d)
						raise AssertionError
					except TypeError:
						pass
			else:
			        res = Tristate(v,d)
		    		assert isinstance(res,_Tristate)

	def test_Tristatedriver(self):
		""" tests whether the driver list is created properly """
		self.cases()
		testdriver = _Tristate(None)
		refdriver = []
		for i in self.val:
			testdriver._val=i
			isinstance(testdriver,_Tristate)
			testdriver.driver()
			refdriver.append(_TristateDriver(_Tristate(i)))
		assert refdriver == testdriver._drivers

	def test_Tristateinit(self):
		""" test for initialisation of _Tristate """
		initcheck = _Tristate(None)
		assert initcheck._drivers == []
		assert initcheck._val == None 

	def testresolve(self):
		""" test to check that if exactly one driver has a not None value 
		    then _next will be the value in driver.Else it will set _next None """
		self.cases()
		for i in self.val:
			Tristateobj = _Tristate(i)
			for j,out in zip(self.Lst,self.Lstout):
				for k in j:
					Tristateobj._val = k
					Tristateobj.driver()
				Tristateobj._resolve()
				assert out == Tristateobj._next
				Tristateobj._drivers = []

	def testinit_Tristatedriver(self):
		""" test for initialisation of _Tristateddriver """
		bus = _Tristate(None)
		k = bus.driver()
		initdrivcheck = _TristateDriver(bus)
		assert initdrivcheck._val == None
		assert initdrivcheck._bus == bus
		assert bus._val == None

	def testinit_DelayedTristate(self):
		""" test for initialisation of _DelayedTristate """
		initdel = _DelayedTristate(None)
		assert initdel._drivers == []
		assert initdel.delay == 1
		assert initdel._val == None