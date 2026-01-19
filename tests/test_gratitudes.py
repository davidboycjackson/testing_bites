from lib.gratitudes import *

def test_gratitudes_add_family():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    assert gratitudes.format() == "Be grateful for: family"
    
def test_gratitudes_three_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("one")
    gratitudes.add("two")
    gratitudes.add("three")
    assert gratitudes.format() == "Be grateful for: one, two, three"