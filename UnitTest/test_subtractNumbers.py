from unittest import TestCase
import Function

class TestSubtractNumbers(TestCase):
    def test_SubtractNumbers(self):
        self.assertEqual(1, Function.SubtractNumbers(3, 4))
        #self.fail()


