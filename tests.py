from add import Rational
import unittest

class TestArithmetic(unittest.TestCase):

    def setUp(self):
        self.rational = Rational()

    def testAdd(self):
        self.assertEqual(4, self.rational.add(2, 2))

    def testSubtract(self):
        self.assertEqual(4, self.rational.subtract(6, 2))

    def testDivide(self):
        self.assertEqual(4, self.rational.divide(8, 2))


    def testMultiply(self):
        self.assertEqual(4, self.rational.multiply(2, 2))

unittest.main()