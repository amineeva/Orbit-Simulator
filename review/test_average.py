from average import average_value

def test_average_value_123(): # this one will pass because it's 3 numbers
    """
    Check that the average of the simple list [1, 2, 3] is 2.0
    """
    assert average_value([1, 2, 3]) == 2.0

def test_average_value_single_one():
    """
    Check that the average value of a single 1 is indeed 1.0.
    """
    assert average_value([1]) == 1.0
