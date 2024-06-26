import pytest
from source.print_promotion import print_promotion

def test_minumum_promotion():
    result = print_promotion(500)
    assert result == 'Free ice cream cone = 1'

def test_midrange_promotion():
    result = print_promotion(850)
    assert result == 'Free chocolate cake = 1'

def test_maximum_promotion():
    result = print_promotion(1250)
    assert result == 'Free ice cream cone = 1 and Free chocolate cake = 1'




def test_low1_promotion():
    result = print_promotion(10)
    assert result == 'Thank you and see you next time'

def test_low2_promotion():
    result = print_promotion(250)
    assert result == 'Thank you and see you next time'

def test_low3_promotion():
    result = print_promotion(490)
    assert result == 'Thank you and see you next time'




def test_double_minimum_promotion():
    result = print_promotion(1000)
    assert result == 'Free ice cream cone = 2'

def test_double_midrange_promotion():
    result = print_promotion(1400)
    assert result == 'Free chocolate cake = 2'

def test_double_maximum_promotion():
    result = print_promotion(2400)
    assert result == 'Free ice cream cone = 2 and Free chocolate cake = 2'

