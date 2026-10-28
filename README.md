# Welcome to bamod 

### About
This is primarily a CLI project that is aimed for folks comfortable with programming, the commadn line, and curious about the integers and little math puzzles. This repo is concerned with the integers under addition, changing the base of an integer, and the integers modulo m under multiplicaiton. Please note i have not tested and developed the negative numbers here yet.
I intentionally am avoiding the operators { //, and % } because I am doing this for fun and wanted to build the modulo function more from scratch.

### Usage

To use this repo you will need python, numpy, and pytest.

Step 1. Download the repo / git clone
Step 2. utilize the makefile with the followng commands 
-  make create_env
-  make activae_env
Step 3a. invoke python in your terminal and run the following
-  python3
-  import bamod
-  gcf(10,15)
-  a_base_b(15,4)
-  mod(12,5)
-  exit()
Step 3b. Open up a filename.py in the downloaded repo and import bamod to use the functions.

Note: this will be a fun tool to have for a jupyter notebook so you can/ maybe i will include jupyter notebooks into the setup here soon.

### The Files Within This Repo

#### Makefile 
This file has some easier UI to setting up the environment 

#### bamod.py  
This is wehre all the funcitons live. 
Within bamod is 
1. gcf : returns the largest common integer factor between integers a and b 
2. mod : returns the number_of_As_in_B and the remainder of A mod B
3. cayley : prints a cayley table of Z/mZ \{0} for any integer m and the factorization of the equivalence class of integer a 
4. build_count_symbol_dict : returns a dictionary of the symbols needed for some base 
5. a_base_b : turns a in base 10 into base b

#### test_bamod.py
This file has some tests to guide dev and establish expectations

### README.md
This file is this file that you're reading. Note to person reading this who writes general text editing code. you should make vim binding toggles for the popular document editors google docs etc.

This project was written completely by a human
