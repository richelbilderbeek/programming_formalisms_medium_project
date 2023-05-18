from src.pfmp.small import is_zero

if __name__ == "__main__":
    print("Show the documentation:")
    print(is_zero.__doc__)

    print("Show how an exception looks like:")
    try:
        is_zero("should be a number")
    except TypeError as e:
        print(e)

    print("Done showing off this package")
