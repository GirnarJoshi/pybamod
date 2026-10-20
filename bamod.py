"""
This Script holds two functions. 
(eventually 3)
it holds a base and a mod functions (eventually a gcd) that work on the natural numbers. 
eventually they will work on the integers too; 
This is meant to be used in the command line. and i made it because i am bored at my job and figuinr out bases and mods algorithmically is fun 
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
        r the remainder / equivalence class representative

    """
    a_temp = a
    ms_in_a = 0 
    r = a
    while (a_temp >= m):
        ms_in_a += 1 
        r = r - m 
        a_temp = a_temp - m 

    print("\n")
    print(f"{a} mod {m} == {r}")
    print(f"{a} = {m}*{ms_in_a} + {r}")
    print("\n")

    return r



# a base m, where a is base 10
def base10_to_base_m( a: int, b: int):
    """
    this function takes an inteer a in base 10 and converts it into base b 

    Arguments: 
        a: the base 10 number that will be converted 
        b: the base it will be converted into
    """
    # Set up the dict of symbols
    #
    symbols = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    base10_to_symbols_dict = {}
    for i in range(len(symbols)):
        base10_to_symbols_dict[i]=symbols[i]
    print(f"15 : {base10_to_symbols_dict[15]}")
    print("\n")

    if (m >10 ):
        print("bases above 10 is not yet supported")
    else:
        a_cpy = a
        n = 0 
        digits = [0]
        # how many digits are we needing with for our final 
        while( a_cpy > pow(b,n) ):
            n+=1 
            digits.append(0)
        digits.pop()
        print(f"n is {n}")
        print(f"digits length is {len(digits)}")

    return 0





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
        base10_to_base_m(a,m)

    else:
        print("Mod Usage: \n python3 bamod.py int mod int \n like, python3 5 mod 3")
        print("Base Usage: \n python3 bamod.py int base int \n like, python3 5 base 3")

