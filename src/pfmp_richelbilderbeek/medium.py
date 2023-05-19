'''
Name                          |Purpose
------------------------------|--------------------------------------------------------
`bubble_sort(x)`              |Returns the sorted elements of `x` using bubble sort
`block_sort(x)`               |Returns the sorted elements of `x` using block sort
`cube_sort(x)`                |Returns the sorted elements of `x` using cube sort
`cocktail_shaker_sort(x)`     |Returns the sorted elements of `x` using cocktail shaker sort
`comb_sort(x)`                |Returns the sorted elements of `x` using comb sort
`cycle_sort(x)`               |Returns the sorted elements of `x` using cycle sort
`exchange_sort(x)`            |Returns the sorted elements of `x` using exchange sort
`gnome_sort(x)`               |Returns the sorted elements of `x` using gnome sort
`heap_sort(x)`                |Returns the sorted elements of `x` using heap sort
`intro_sort(x)`               |Returns the sorted elements of `x` using intro sort
`insertion_sort(x)`           |Returns the sorted elements of `x` using insertion sort
`is_sorted(x)`                |Returns `True` if the elements of `x` are in ascending order
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
    if (len(fs) == 0): return False;
    return True

def get_sorting_functions():
    """
    Get a list with all the sorting functions.
    
    Each sorting function is a pure function 
    that takes 1 argument
    and returns the sorted argument
    """
    # check_are_functions(functions)
    return True

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
    # check_are_functions(functions)
    return True

def is_function(f):
    """
    Determines if `f` is a function.
    Returns `True` if `f` is a function
    """
    return hasattr(f, '__call__')

def is_sorted(data):
    """
    Determines if `data` is sorted.
    Returns `True` if the data is sorted
    """
    return data == sorted(data)

def silly_sort(data):
    """
    Sorts `data` in a silly way.
    Returns the `data` after sorting it.
    """
    return True

def stupid_sort(data):
    """
    Sorts `data` in a stupid way.
    Returns the `data` after sorting it.
    """
    return True

