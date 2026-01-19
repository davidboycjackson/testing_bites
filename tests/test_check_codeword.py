from lib.check_codeword import *

def test_check_codeword_is_horse():
    assert check_codeword("horse") == "Correct! Come in."
    
def test_check_codeword_is_home():
    assert check_codeword("home") == "Close, but nope."
    
def test_check_codeword_is_mouse():
    assert check_codeword("mouse") == "WRONG!"