from bamod import mod, build_count_symbol_dict, a_base_b 

def test_1():
    assert ( mod(5,2) == 3,1 ) 

def test_2():
    assert ( a_base_b(5,10) == '5')

def test_3():
    assert ( a_base_b(3,2) == '11')
