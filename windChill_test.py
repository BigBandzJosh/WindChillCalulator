import unittest
import windChill

class TestWindChill(unittest.TestCase):
    def test_windChill(self):
       self.assertEqual(windChill.WindChill(-10, 1), -10.587)
       self.assertAlmostEqual(windChill.WindChill(-10, 6), -13.521, places=3)