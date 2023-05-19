import unittest

from src.pfmp_richelbilderbeek.medium import get_speed_measurements

class TestMedium(unittest.TestCase):
    def test_get_speed_measurements(self):
        self.assertIsNotNone(get_speed_measurements.__doc__)
