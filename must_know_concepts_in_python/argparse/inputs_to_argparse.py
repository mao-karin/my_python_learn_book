#using optional arguments for the examples

#taking a string as an input..................................................................................
import argparse

parser = argparse.ArgumentParser(description='Name greeting')
parser.add_argument('-n', '--name', type=str,  help='Enter your name')
args = parser.parse_args()

print("Hi my name is {}".format(args.name))

#run like this: python inputs_to_argparse.py -n <Your Name>

#taking one input (int) per argument...........................................................................
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cyliner')
parser.add_argument('-r', '--radius', type=int, required=True, help='Radius of Cyliner')
parser.add_argument('-H','--height', type=int, required=True, help='Height of Cylinder')
args = parser.parse_args()

vol = (math.pi) * (args.radius**2) * (args.height)
print("The volume is {}".format(vol))

#run like this: python inputs_to_argparse.py -r 2 -H 4

#taking 2 inputs (int) in an agrument..........................................................................
#different values of nargs may cause metavar to be used mulitple times
#Providing a tuple to metavar specifies a different display for each of the arguments

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'),
                        help='Image size')
args = parser.parse_args()
print(args.size)

#run like this: python inputs_to_argparse.py -s 2 4
#outputs a tuple (2,4)

#take multiple inputs in an argument...........................................................................
#like -a 1 2 3 4

import argparse

p = argparse.ArgumentParser()
p.add_argument('-a', nargs="+", type=int)
args = p.parse_args()

# check if input is valid
set_a = set(args.a)
set_b = set(args.b)

# check if "a" is in proper range.
if len(set_a - set(range(1, 51))) > 0: # can use also min(a)>=1 and max(a)<=50
    raise Exception("set a not in range [1,50]")

# check if "b" is in "a"
if len(set_b - set_a) > 0:
    raise Exception("set b not entirely in set a")

# you could even skip len(...) and leave just operations on sets

#runs:
#python arg.py  -a 1 2 3 4 -b 2 20
#Exception: set b not entirely in set a

#python arg.py  -a 1 2 3 4 60 -b 2
#Exception: set a not in range [1,50]

#valid run:
#python arg.py  -a 1 2 3 4 -b 2 3

#take multiple inputs for an argument and separate it by "," instead of "space"........................................
#run like this: python inputs_to_argparse.py -l 1,2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--list', type=str, required=True, help="enter number list separated by comma")
args = parser.parse_args()
l1_list = args.list.split(',') # ['1','2','3','4']... string list
num_list= [int(x) for x in l1_list] #converts it to int .....[1,2,3,4]
print(num_list)

#run like this: python inputs_to_argparse.py -l 1,2
#output = [1,2]
#directly putting type=int doesnt work for split().. well i couldnt make it work at least

#take multiple inputs as choices............................................................................
#use argparse's {choices} parameter, and allow the user to input any number of items from choices
#For example if choices is [1,2,3], I would like the following to be valid:
#--arg 1
#--arg 1,2
#--arg 1,3

import argparse, sys
print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('--arg', nargs='+', choices=[1,2,3], type=int)
args = parser.parse_args()
print(args)

#this will run the script with the choices provided but will not run comma separated ones
#run like this: python input_to_argsparse.py --arg 1 or python input_to_argsparse.py --arg 1 3 2 1

#to add comma, change choices to strings and drop int type
import argparse, sys
print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('--arg', nargs='+', choices=['1','2','3','1,2','2,3','1,2,3'])
args = parser.parse_args()
print(args)

#take a file location input.................................................................................
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, metavar="input", help="path to file")
args = ap.parse_args()

input_path = args.input 

#to check
print(input_path)

#run like this: python inputs_to_argparse.py <input-filename>      >>for this the file needs to be in same folder as the script
#or run like this: python inputs_to_argparse.py <path to the file>
