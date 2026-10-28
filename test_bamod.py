from bamod import mod, build_count_symbol_dict, a_base_b, gcf


# Testing Base 
#
def test_base_1():
    assert ( a_base_b(5,10) == '5')

def test_base_2():
    assert ( a_base_b(3,2) == '11')



# Testing mod 
#
def test_mod_1():
    assert ( mod(5,2) == (2,1) ) 

def test_mod_2():
    assert ( mod(2,5) == (0, 2) )



# Testing GCF 
# gcf of 1
def test_gcf_1():
    assert ( gcf(5,7) == 1 )

def test_gcf_2():
    assert ( gcf(7,5) == 1 )
# gcf of not 1 
def test_gcf_3():
    assert ( gcf(10,50) == 10 )

def test_gcf_4():
    assert ( gcf(50,10) == 10 )

    # tests where there are integers smaller than a and larger than the gcf
def test_gcf_5():
    assert ( gcf(15,20) == 5 )

def test_gcf_6():
    assert ( gcf(20,15) == 5 )



# Testing Cayley Tables 
#




