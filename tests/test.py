import unittest
from code import *

class TestCases(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(1, 1)


	'''
	Add your own test cases here
	function name must start with test_
	'''
	
# 	def test_addition(self):
# 		self.assertEqual(5, add(2,3))
# 		self.assertEqual(0, add(-1,1))
		
# 	def test_subtraction(self):
# 		self.assertEqual(3, sub(5,2))
# 		self.assertEqual(-4, sub(5,9))

if __name__ == "__main__":
	unittest.main()
