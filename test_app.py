import unittest
from app import check_parentheses
import sys

class ParenthesesTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(check_parentheses("(8*9)**4"), True)
	def test2(self):
		self.assertEqual(check_parentheses("(9+8*2"), False)
	def test3(self):
		self.assertEqual(check_parentheses("9/4"), True)
	def test4(self):
		self.assertEqual(check_parentheses("(8*5))"), False)
	def test5(self):
		self.assertEqual(check_parentheses("(2+1)*445+(9/7)*1"), True)

if __name__ == '__main__':
	unittest.main()