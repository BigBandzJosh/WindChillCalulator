import unittest
import windChill

class TestWindChill(unittest.TestCase):
    def test_windChill(self):
       self.assertEqual(windChill.WindChill(-10, 1), -10.94468258)