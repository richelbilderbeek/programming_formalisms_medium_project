if __name__ == "__main__":
    print("Start of tests")
    test_are_numbers()
    test_are_strings()
    test_check_are_numbers()
    test_check_different()
    test_check_equal()
    test_check_is_number()
    test_check_is_probability()
    test_check_is_string()
    test_divide_safely()
    test_is_dividable_by_three()
    test_is_even()
    test_is_number()
    test_is_odd()
    test_is_probability()
    test_is_string()    
    test_is_zero()
    
    # Show the documentation
    print(is_zero.__doc__)

    # Show an exception
    try:
        is_zero("should be a number")
    except TypeError as e:
        print(e)
    
    print("All tests passed")
