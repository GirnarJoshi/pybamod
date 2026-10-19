"""
This Script holds two functions. 
it holds a base and a mod functions that work on the natural numbers. 
eventually they will work on the integers too; 
This is meant to be used in the command line. and i made it because i am bored at my job and figuinr out bases and mods algorithmically is fun 
I will eventually add a Cayley Table for Z/mZ\{0} under * vizualizer and factor explainer 
"""
import sys  

symbols = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
base_10_symbols_dict = {}


try:
    arg0 = sys.argv[0]
    arg1 = int(sys.argv[1])
    arg2 = sys.argv[2]
    arg3 = int(sys.argv[3])
except IndexError as ie:
    print(f"Error: {ie}, usage ==> python3 pymod.py [int] mod [int] ")
    sys.exit(1)

# print(f"arg0 {arg0}, arg1 {arg1},arg2 {arg2}, arg3 {arg3}")

m = arg3
a = arg1
assert(type(arg1) == int )
assert(type(arg3) == int )

def mod( a: int , m: int):
    a_temp = a
    ms_in_a = 0 
    r = a
    while (a_temp >= m):
        ms_in_a += 1 
        r = r - m 
        a_temp = a_temp - m 
    print(f"{a} mod {m} == {r}")
    print(f"{a} = {m}*{ms_in_a} + {r}")



# a base m, where a is base 10
def base10_to_m( a: int, m: int):

    if (m >10 ):
        print("bases above 10 is not yet supported")
    else:
        a_cpy = a
        n = 0 
        digits = [0]
        # how many digits are we needing with for our final 
        while( a_cpy > pow(m,n) ):
            n+=1 
            digits.append(0)
        digits.pop()
        print(f"n is {n}")
        print(f"digits length is {len(digits)}")










if (arg2 == "mod"):
    mod(a,m)

if ( arg2 == "base"):
    base10_to_m(a,m)

else:
    print("Mod Usage: \n python3 bamod.py int mod int \n like, python3 5 mod 3")
    print("Base Usage: \n python3 bamod.py int base int \n like, python3 5 base 3")

