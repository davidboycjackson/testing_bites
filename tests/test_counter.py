from lib.counter import *

def test_counter_adds_five():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
    
def test_counter_ten_and_twenty_is_thirty():
    counter = Counter()
    counter.add(10)
    counter.add(20)
    assert counter.report() == "Counted to 30 so far.", "Returns 30 having added 10 and 20"