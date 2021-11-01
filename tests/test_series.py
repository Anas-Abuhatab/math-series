from math_series.series import fibonacci,lucas,sum_series

def test_fibonacci_8():
    actual = fibonacci(8)
    expected = 21
    assert expected == actual

def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert expected == actual

def test_sum_series_fibonacci_8():
    actual = sum_series(8)
    expected = 21
    assert expected == actual

def test_sum_series_lucas_5():
    actual = sum_series(5,2,1)
    expectd = 11
    assert expectd == actual

def test_sum_series_other_eight_seven_six():
    actual = sum_series(8,7,6)
    expected = 217
    assert expected == actual
