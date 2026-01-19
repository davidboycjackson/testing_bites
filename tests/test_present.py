import pytest
from lib.present import *

def test_present_wrap_then_unwrap():
    present = Present()
    present.wrap("a gift")
    present.unwrap() == "a gift"

def test_present_wrap_two_gifts():
    present = Present()
    present.wrap("gift one")
    with pytest.raises(Exception) as e:
        present.wrap("gift two")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    
def test_present_unwrap_empty_gift():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."
    