import unittest
import windChill

class TestWindChill(unittest.TestCase):
    def test_windChill(self):
       self.assertEqual(windChill.WindChill(-10, 1), -10.587)

    def test_windChill2(self):
        self.assertAlmostEqual(windChill.WindChill(-10, 0.539957, 'C', 'knots'), -10.587, places=3)

    def test_windChill3(self):
        self.assertEqual(windChill.WindChill(14, 1, 'F', 'kmh'), -10.587)

    def test_windChill4(self):
        self.assertAlmostEqual(windChill.WindChill(-10, 6, 'C', 'kmh'), -13.521, places=3)

    def test_windChill5(self):
        self.assertIsNone(windChill.WindChill(10, 0.539957, 'C', 'knots'), None)
        

