from random import seed
from random import shuffle
from pandas import DataFrame
from time import time

'''
Name                          |Purpose
------------------------------|--------------------------------------------------------
`bubble_sort(x)`              |Returns the sorted elements of `x` using bubble sort
`block_sort(x)`               |Returns the sorted elements of `x` using block sort
`cube_sort(x)`                |Returns the sorted elements of `x` using cube sort
`cocktail_shaker_sort(x)`     
`comb_sort(x)`                |Returns the sorted elements of `x` using comb sort
`cycle_sort(x)`               |Returns the sorted elements of `x` using cycle sort
`exchange_sort(x)`            |Returns the sorted elements of `x` using exchange sort
`gnome_sort(x)`               |Returns the sorted elements of `x` using gnome sort
`heap_sort(x)`                |Returns the sorted elements of `x` using heap sort
`intro_sort(x)`               |Returns the sorted elements of `x` using intro sort
`insertion_sort(x)`           |Returns the sorted elements of `x` using insertion sort
`is_sorting_method(m)`        |Returns `True` if `m` is a sorting method
`library_sort(x)`             |Returns the sorted elements of `x` using library sort
`merge_sort(x)`               |Returns the sorted elements of `x` using merge sort
`odd_even_sort(x)`            |Returns the sorted elements of `x` using odd-even sort
`quick_sort(x)`               |Returns the sorted elements of `x` using quick sort
`selection_sort(x)`           |Returns the sorted elements of `x` using selection sort
`shell_sort(x)`               |Returns the sorted elements of `x` using shell sort
`tim_sort(x)`                 |Returns the sorted elements of `x` using tim sort
`tree_sort(x)`                |Returns the sorted elements of `x` using tree sort
`patience_sort(x)`            |Returns the sorted elements of `x` using patience sort
`smooth_sort(x)`              |Returns the sorted elements of `x` using smooth sort
`sort(x)`                     |Returns the sorted elements of `x`
`sort(x, m)`                  |Returns the sorted elements of `x` using method `m`
`strand_sort(x)`              |Returns the sorted elements of `x` using strand sort
`tournament_sort(x)`          |Returns the sorted elements of `x` using tournament sort
'''

"""
These are all the simple functions of The Medium Project
"""

def are_functions(fs):
    """
    Determines if `fs` is one or more functions.
    Returns `True` if `f` is one or more functions
    """
    if (not is_list(fs)): 
        return False
    if (len(fs) == 0): 
        return False
    for i in range(len(fs)):
        if not is_function(fs[i]):
            return False
    return True

def are_speed_measurements(x):
    """
    Determines if `x` is a table of speed measurements.

    The table of speed measurements must be a dictionary.

    Its three expected keys are:
     * `function_name`
     * `data_length`
     * `runtime_speed_secs`
    
    Each key element is a list.
    These three lists have an equal length.

    Returns `True` if `x` is a table of speed measurements.
    """
    if not isinstance(x, dict): 
        return False
    if (len(x) != 3): 
        return False
    these_keys = list(x.keys())
    expected_keys = ["function_name", "data_length", "runtime_speed_secs"]
    if (these_keys != expected_keys): 
        return False
    if (len(x["function_name"]) != len(x["data_length"])): 
        return False
    if (len(x["function_name"]) != len(x["runtime_speed_secs"])): 
        return False
    return True

def get_datas(rng_seed = 42, data_lengths = [9, 99, 999]):
    """
    Get a list of datasets (hence, the reduplicated/Gollumese plural)
    
    Each dataset is list of numbers, 
    which can be used to illustrate sorting algorithms.
    """
    seed(rng_seed)
    datas = []
    for data_length in data_lengths:
        data = [x * x for x in range(0, data_length)]
        shuffle(data)
        datas.append(data)
    return datas

def get_sorting_functions():
    """
    Get a list with all the sorting functions.
    
    Each sorting function is a pure function 
    that takes 1 argument
    and returns the sorted argument
    """
    return [silly_sort, stupid_sort]

def get_speed_measurements(functions, datas):
    """
    Measure how long the runtime is of each function,
    per each data.

    Parameters:
    `functions`: two or more functions 
        that can work on an element of `datas`
    `datas`: one or more sets of data (hence, the 
        reduplicated/Gollumese plural)
    
    Returns a dict with three columns:
      1. The function index (first function has index zero)
      2. The data index (first data has index zero)
      3. The time in seconds the function took to process the data
    """
    speed_measurements = {
        "function_name": [],
        "data_length": [],
        "runtime_speed_secs": []
    }
    for f in functions:
        for data in datas:
            speed_measurements["data_length"].append(len(data))
            speed_measurements["function_name"].append(f.__name__)
            start = time()
            f(data)
            end = time()
            t = end - start
            speed_measurements["runtime_speed_secs"].append(t)

    return speed_measurements

def get_test_datas(rng_seed = 42):
    """
    Get a list of datasets (hence, the reduplicated/Gollumese plural)
    
    Each dataset is list of numbers, 
    which can be used to illustrate sorting algorithms.
    """
    return get_datas(rng_seed = rng_seed, data_lengths = [2, 3, 4])

def get_test_speed_measurements():
    """
    Returns a collection of speed measurements, to be used in tests
    """
    return {
        "function_name": ["silly_sort", "stupid_sort"],
        "data_length": [0, 1],
        "runtime_speed_secs": [0.1, 0.2]
    }

def is_dict(x):
    """
    Determines if `x` is a dict.
    Returns `True` if `x` is a dict.
    """
    return type(x) == dict

def is_function(f):
    """
    Determines if `f` is a function.
    Returns `True` if `f` is a function
    """
    return hasattr(f, '__call__')

def is_list(x):
    """
    Determines if `x` is a list.
    Returns `True` if `x` is a list.
    """
    return type(x) == list

def is_sorted(data):
    """
    Determines if `data` is sorted.
    Returns `True` if the data is sorted
    """
    return data == sorted(data)

def save_dict(x, csv_filename):
    """
    Saves the dictionary `x` to a file named `csv_filename`
    """
    assert is_dict(x)
    df = DataFrame.from_dict(x)
    df.to_csv(csv_filename, index = False)
    pass

def save_speed_measurements(speed_measurements, csv_filename):
    """
    Saves the `speed_measurements` to a file named `csv_filename`
    """
    assert are_speed_measurements(speed_measurements)
    save_dict(
        x = speed_measurements, 
        csv_filename = csv_filename
    )

def silly_sort(data):
    """
    Sorts `data` in a silly way.
    Returns the `data` after sorting it.
    """
    sorted_data = stupid_sort(data)

    # Just to be super sure it is sorted :-)
    doubly_sorted_data = sorted(sorted_data)
    return doubly_sorted_data

def stupid_sort(data):
    """
    Sorts `data` in a stupid way.
    Returns the `data` after sorting it.
    """
    while True:
        if (is_sorted(data)): 
            return data
        shuffle(data)

