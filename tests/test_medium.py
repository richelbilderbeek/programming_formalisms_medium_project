import unittest


from src.pfmp_richelbilderbeek.medium import are_functions
from src.pfmp_richelbilderbeek.medium import get_datas
from src.pfmp_richelbilderbeek.medium import get_sorting_functions
from src.pfmp_richelbilderbeek.medium import get_speed_measurements
from src.pfmp_richelbilderbeek.medium import is_function
from src.pfmp_richelbilderbeek.medium import is_list
from src.pfmp_richelbilderbeek.medium import is_sorted
from src.pfmp_richelbilderbeek.medium import silly_sort
from src.pfmp_richelbilderbeek.medium import stupid_sort

class TestMedium(unittest.TestCase):

    def test_are_functions(self):
        self.assertIsNotNone(are_functions.__doc__)
        self.assertTrue(are_functions( [silly_sort, stupid_sort]))
        self.assertTrue(are_functions( [silly_sort]))
        self.assertFalse(are_functions( [] ))
        self.assertFalse(are_functions(3.14))
        self.assertFalse(are_functions("Hello"))

    def test_get_datas(self):
        self.assertIsNotNone(get_datas.__doc__)
        self.assertTrue(is_list(get_datas()))
        self.assertEqual(get_datas(42), get_datas(42))
        self.assertNotEqual(get_datas(42), get_datas(43))

    def test_get_sorting_functions(self):
        self.assertIsNotNone(get_sorting_functions.__doc__)
        self.assertTrue(are_functions(get_sorting_functions()))

    def test_get_speed_measurements(self):
        self.assertIsNotNone(get_speed_measurements.__doc__)

    def test_is_function(self):
        self.assertIsNotNone(is_function.__doc__)
        self.assertTrue(is_function(is_function))
        self.assertFalse(is_function(42))

    def test_is_list(self):
        self.assertIsNotNone(is_list.__doc__)

    def test_is_sorted(self):
        self.assertIsNotNone(is_sorted.__doc__)
        self.assertTrue(is_sorted([1, 2]))
        self.assertTrue(is_sorted([1]))
        self.assertFalse(is_sorted([2, 1]))

    def test_silly_sort(self):
        self.assertIsNotNone(silly_sort.__doc__)

    def test_stupid_sort(self):
        self.assertIsNotNone(stupid_sort.__doc__)

