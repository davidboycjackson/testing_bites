from lib.string_builder import *

def test_string_builder_hello_size():
    builder = StringBuilder()
    builder.add("Hello")
    assert builder.size() == 5
    assert builder.output() == "Hello"
    
def test_string_builder_numbers_to_five():
    builder = StringBuilder()
    builder.add("One")
    builder.add("Two")
    builder.add("Three")
    builder.add("Four")
    builder.add("Five")
    assert builder.size() == 19
    assert builder.output() == "OneTwoThreeFourFive"