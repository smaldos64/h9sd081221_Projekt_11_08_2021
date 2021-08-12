from unittest import TestCase

import Function

class TestFunction(TestCase):
    def test_AddNumbers(self):
        self.assertEqual(3, Function.AddNumbers(1, 2))
        self.assertEqual(3, Function.AddNumbers(1, 2))
        self.assertEqual(7, Function.AddNumbers(3, 4))
        #self.fail()

    def test_SubtractNumbers(self):
        self.assertEqual(-1, Function.SubtractNumbers(3, 4))
        #self.fail()

    def test_MultiplyNumbers(self):
        self.assertEqual(12, Function.MultiplyNumbers(3, 4))
        #self.fail()






