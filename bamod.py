"""
This Script holds two primary functions. 
(eventually 3)
it holds a base and a mod functions (eventually a gcd) that work on the natural numbers. 
eventually they will work on the integers too; 
This is meant to be used in the command line. and i made it because figuing out bases and mods algorithmically is fun 
I will eventually add a Cayley Table for Z/mZ\{0} under * vizualizer and factor explainer 
"""
import sys  

def mod( a: int , m: int):
    """
    finds the remainder of integer a in modulo m, where  
    a mod m = r. and for some integer b,  a = b * m + r  

    Arguments:
        a: integer of interest
        m: modulo of interest 
    Returns:
        b: the number of times m fits into a 
        ms_in_a: the remainder / equivalence class representative

    """
    a_temp = a
    ms_in_a = 0 
    r = a
    while (a_temp >= m):
        ms_in_a += 1 
        r = r - m 
        a_temp = a_temp - m 

    print(f"{a} mod {m} == {r}")
    print(f"{a} = {m}*{ms_in_a} + {r}")
    print("\n")

    return ms_in_a, r

def build_count_symbol_dict(m:int):
    """
    This is a helper funct to just make the dictionary of symbols for a needed base

    Arguments:
        m: int: the base you need symbols for 
    Returns:
        dictionary key: int 0 to m-1 value: symbol for that count
    """
    # Set up the dict of symbols
    #
    symbols = ['0','1','2','3','4','5','6','7',
               '8','9','a','b','c','d','e','f',
               'g','h','i','j','k','l','m','n',
               'o','p','q','r','s','t','u','v',
               'w','x','y','z','å','∫','ç','∂',
               'ƒ','∆','µ','ø','π','œ','ß','†',
               '∑','≈','Ω','Å','Ç','Î','∏','◊']
    
    b10_to_symbols = {}
    for i in range(m):
        b10_to_symbols[i]=symbols[i]
        print(f"i:{i}, symbols[{i}]:{symbols[i]}")
    print("\n")
   
    return b10_to_symbols

def a_base_b( a: int, b: int):
    """
    this function takes an inteer a in base 10 and converts it into base b 

    Arguments: 
        a:int: the base 10 number that will be converted 
        b:int: the base it will be converted into ( also expressed in base 10 lol )
    Returns:
        a_in_base_b:str: the count value of a represented in base b
    """
    
    if (b >56 ):
        print("bases above 56 are not yet supported")

    else:
        # step 1: get symbols
        symbol_dict = build_count_symbol_dict(b)

        # step 2: find num digits
        n_digits = 1
        # num digits is 1 larger than the the max power digit 
        while a >= pow(b, n_digits):
            n_digits += 1

        # step 3: fill digits large to small 
        # digits will b^n_digits-1,b^n_digits-2,b^n_digits-3,b^n_digits-4,...
        digits = [0]
        for i in range(n_digits - 1):
            digits.append(0) # fill w 0s for now.
        assert(len(digits) == n_digits)
        
        a_cpy = a

        # range(start, stop, step)
        for i in range(n_digits):
            # how many b^n_digits-i are in a_cpy 
            
            ms_in_a, r = mod(a_cpy, pow(b, n_digits - i - 1))

            digits[i] = symbol_dict[ms_in_a] 
            # subtract that number from a_cpy (same as using the remainder)
            a_cpy = r 


        a_in_base_b=""
        for i in range(n_digits):
            a_in_base_b += (str(digits[i]))

        print(f" {a} in base {b} is {a_in_base_b}")
        
        for i in range(n_digits):
            print(f"{digits[i]}*{b}^{n_digits-i}")

        return a_in_base_b

if __name__ == "__main__":

    # handle the CL arguments 
    #
    # python3 bamod.py int mod/base int cayley
    # argv[]   [0]     [1]   [2]    [3]  [4]
    try:
        print(f" num CL args: {len(sys.argv)}")
        for a in range(len(sys.argv)):
            print(f" arg num {a} : {sys.argv[a]} ")

        assert(len(sys.argv) >= 4)

    except AssertionError as ie:
        print("\n")
        print(f"Error: {ie}, usage ==> python3 pymod.py [int] mod/base [int] caley(optional) ")
        sys.exit(1)

    a = int(sys.argv[1])
    m = int(sys.argv[3])

    print("\n")
    print(f" a={a} tool={sys.argv[2]} m={m}")

    # Run the Functions 
    #
    if (sys.argv[2] == "mod"):
        mod(a,m)

    elif (sys.argv[2] == "base"):
        a_base_b(a,m)

    else:
        print("Mod Usage: \n python3 bamod.py int mod int \n like, python3 5 mod 3")
        print("Base Usage: \n python3 bamod.py int base int \n like, python3 5 base 3")
