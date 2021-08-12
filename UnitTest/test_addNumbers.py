from unittest import TestCase

import Function

class TestAddNumbers(TestCase):
    def test_AddNumbers(self):
        self.assertEqual(6, Function.AddNumbers(1, 2))
        #self.fail()
