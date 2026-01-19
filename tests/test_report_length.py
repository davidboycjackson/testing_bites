from lib.report_length import *

def test_report_length_ten_long():
    assert report_length("ABCDEFGHIJ") == "This string was 10 characters long."
    
def test_report_length_fifteen_long():
    assert report_length("This is a test!") == "This string was 15 characters long."