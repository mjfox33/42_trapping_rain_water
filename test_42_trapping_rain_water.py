import code_42_trapping_rain_water as c

def test_example_1():
    s = c.Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_example_2():
    s = c.Solution()
    assert s.trap([4,2,0,3,2,5]) == 9