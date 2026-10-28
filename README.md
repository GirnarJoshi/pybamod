# Welcome to bamod 

This repo is concerned with the integers under addition, changing the base of an integer, and the integers modulo m under multiplicaiton.
I intentionally am avoiding the operators { //, and % } because I am doing this for fun. 

Within this repo are several files 
* Makefile
This file has some easier UI to setting up the environment 

* bamod.py 
This is wehre all the funcitons live. 
Within bamod is 
1. gcf : returns the largest common integer factor between integers a and b 
2. mod : returns the number_of_As_in_B and the remainder of A mod B
3. cayley : prints a cayley table of Z/mZ \{0} for any integer m and the factorization of the equivalence class of integer a 
4. build_count_symbol_dict : returns a dictionary of the symbols needed for some base 
5. a_base_b : turns a in base 10 into base b

