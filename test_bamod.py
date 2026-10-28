from bamod import mod, build_count_symbol_dict, a_base_b, gcf
#
# Testing Base 
def test_1():
    assert ( a_base_b(5,10) == '5')

def test_2():
    assert ( a_base_b(3,2) == '11')

# Testing mod 
def test_6():
    assert ( mod(5,2) == (2,1) ) 


# Testing GCF 
# gcf of 1
def test_7():
    assert ( gcf(5,7) == 1 )

def test_8():
    assert ( gcf(7,5) == 1 )
# gcf of not 1 
def test_9():
    assert ( gcf(10,50) == 10 )

def test_10():
    assert ( gcf(50,10) == 10 )

    # tests where there are integers smaller than a and larger than the gcf
def test_11():
    assert ( gcf(15,20) == 5 )

def test_12():
    assert ( gcf(20,15) == 5 )

