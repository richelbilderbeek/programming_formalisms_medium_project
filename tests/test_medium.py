import os.path
import unittest

from src.pfmp_richelbilderbeek.medium import (
    are_functions,
    are_speed_measurements,
    get_datas,
    get_sorting_functions,
    get_speed_measurements,
    get_test_datas,
    get_test_speed_measurements,
    is_dict,
    is_function,
    is_list,
    is_sorted,
    save_dict,
    save_speed_measurements,
    silly_sort,
    stupid_sort,
)


class TestMedium(unittest.TestCase):

    def test_are_functions(self):
        assert are_functions.__doc__ is not None
        assert are_functions([silly_sort, stupid_sort])
        assert are_functions([silly_sort])
        assert not are_functions([])
        assert not are_functions(3.14)
        assert not are_functions("Hello")

    def test_are_speed_measurements(self):
        assert are_speed_measurements.__doc__ is not None
        assert are_speed_measurements(get_test_speed_measurements())
        assert not are_speed_measurements(0.1)
        assert not are_speed_measurements({"x": 1.0})
        assert not are_speed_measurements({"x": 1.0, "y": 2.0, "z": 3.0})
        nasty_data_1 = {
            "function_index": [0, 1, 234567], # Oops
            "data_length": [0, 0],
            "runtime_speed_secs": [0.1, 0.2],
        }
        assert not are_speed_measurements(nasty_data_1)
        nasty_data_2 = {
            "function_index": [0, 1],
            "data_length": [0, 0, 123456789], # Oops
            "runtime_speed_secs": [0.1, 0.2],
        }
        assert not are_speed_measurements(nasty_data_2)
        nasty_data_3 = {
            "function_index": [0, 1],
            "data_length": [0, 0],
            "runtime_speed_secs": [0.1, 0.2, 0.3456789], # Oops
        }
        assert not are_speed_measurements(nasty_data_3)

    def test_get_datas(self):
        assert get_datas.__doc__ is not None
        assert is_list(get_datas())
        assert get_datas(42) == get_datas(42)
        assert get_datas(42) != get_datas(43)

    def test_get_sorting_functions(self):
        assert get_sorting_functions.__doc__ is not None
        assert are_functions(get_sorting_functions())

    def test_get_speed_measurements(self):
        assert get_speed_measurements.__doc__ is not None
        speed_measurements = get_speed_measurements(
            datas = get_test_datas(),
            functions = get_sorting_functions(),
        )
        assert are_speed_measurements(speed_measurements)

    def test_get_test_datas(self):
        assert get_test_datas.__doc__ is not None
        assert is_list(get_test_datas())
        assert get_test_datas(42) == get_test_datas(42)
        assert get_test_datas(42) != get_test_datas(43)

    def test_get_test_speed_measurements(self):
        assert get_test_speed_measurements.__doc__ is not None
        assert isinstance(get_test_speed_measurements(), dict)

    def test_is_dict(self):
        assert is_dict.__doc__ is not None
        assert is_dict({"X": 3.14})
        assert not is_dict(3.14)
        assert not is_dict([3.14])

    def test_is_function(self):
        assert is_function.__doc__ is not None
        assert is_function(is_function)
        assert not is_function(42)

    def test_is_list(self):
        assert is_list.__doc__ is not None
        assert not is_list(42)


    def test_is_sorted(self):
        assert is_sorted.__doc__ is not None
        assert is_sorted([1, 2])
        assert is_sorted([1])
        assert not is_sorted([2, 1])
        assert not is_sorted(get_datas()[0])

    def test_save_dict(self):
        assert save_dict.__doc__ is not None
        csv_filename = "temp_save_dict.csv"
        if (os.path.isfile(csv_filename)):
            os.remove(csv_filename)
        assert not os.path.isfile(csv_filename)

        save_dict(
            x = { "X": [1, 2, 3], "Y": [4, 5, 6]},
            csv_filename = csv_filename,
        )
        assert os.path.isfile(csv_filename)
        os.remove(csv_filename)

    def test_save_speed_measurements(self):
        assert save_speed_measurements.__doc__ is not None
        csv_filename = "temp_save_speed_measurements.csv"
        if (os.path.isfile(csv_filename)):
            os.remove(csv_filename)
        assert not os.path.isfile(csv_filename)
        save_speed_measurements(
            speed_measurements = get_test_speed_measurements(),
            csv_filename = csv_filename,
        )
        assert os.path.isfile(csv_filename)
        os.remove(csv_filename)



    def test_silly_sort(self):
        assert silly_sort.__doc__ is not None
        data = get_datas()[0]
        assert not is_sorted(data)
        sorted_data = silly_sort(data)
        assert is_sorted(sorted_data)


    def test_stupid_sort(self):
        assert stupid_sort.__doc__ is not None
        data = get_datas()[0]
        assert not is_sorted(data)
        sorted_data = stupid_sort(data)
        assert is_sorted(sorted_data)

