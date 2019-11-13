'''import unittest class to enable all the functionality to test the cases'''
import unittest
from unittest import TestCase
import tan_func


class TestTan(TestCase):
    """class to test the use case"""
    def test_tan_fun(self):
        """function to test against expected output"""
        self.assertEqual(tan_func.tan_fun(90), -1.995200412)
        self.assertEqual(tan_func.tan_fun(-90), 1.995200412)
        self.assertEqual(tan_func.tan_fun(0), 0.0)
        self.assertEqual(tan_func.tan_fun(1), 1.557407725)
        self.assertEqual(tan_func.tan_fun(56), -0.611273688)


if __name__ == '__main__':
    unittest.main()
