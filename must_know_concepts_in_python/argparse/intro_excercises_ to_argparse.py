#Positional arguments - the arguments have to be inputted according to how it is positioned in teh code. Order matters!
#Optional arguments- uses a flag (ex: -h,--help) to dteremine where the value will be parsed to. Order doesn't matter as long as you use the flag before it!

#reference video: https://www.youtube.com/watch?v=cdblJqEUDNo

#the program calculates volume of a cylinder given radius and height
#volume= (pi) * (radius**2) * (height)                ** is exponent


#code without argparse.......................................................................................................
import math                                 #to get value of pi

def cylinder_volume(radius,height):
    vol = (math.pi) * (radius**2) * (height)
    return vol

if __name__ =='___main___':
    print (cylinder_volume(2,4))              #output: 50.27


#code with argparse (positional arguments)...................................................................................
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cyliner')
parser.add_argument('radius', type=int, help='Radius of Cyliner')
parser.add_argument('height', type=int, help='Height of Cylinder')
args = parser.parse_args()

def cylinder_volume(radius,height):
    vol = (math.pi) * (radius**2) * (height)
    return vol

if __name__ =='___main___':
    print (cylinder_volume(args.radius,args.height))              

#run like this: python intro_to_argparse.py 2 4
#output: 50.27

#code with argparse (optional arguments).........................................................................................
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cyliner')
parser.add_argument('-r', '--radius', type=int,  help='Radius of Cyliner')
parser.add_argument('-H','--height' type=int, help='Height of Cylinder')
args = parser.parse_args()

def cylinder_volume(radius,height):
    vol = (math.pi) * (radius**2) * (height)
    return vol

if __name__ =='___main___':
    print (cylinder_volume(args.radius,args.height))

#run like this: python intro_to_argparse.py -r 2 -H 4
#-r is like a shortcut
#run like this: python intro_to_argparse.py --radius 2 --height 4
#output: 50.27

#to clean up the code a little more:
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cyliner')
parser.add_argument('-r', '--radius', type=int, metavar='', required=True,  help='Radius of Cyliner')
parser.add_argument('-H','--height' type=int, metavar='', required=True, help='Height of Cylinder')
args = parser.parse_args()

def cylinder_volume(radius,height):
    vol = (math.pi) * (radius**2) * (height)
    return vol

if __name__ =='___main___':
    print (cylinder_volume(args.radius,args.height))

#metavar is used to clean clutters/formatting
#required is used to set requires values to variables to run the program. If it is kept optional, it will assign a None value to it.

#Mutually exclusive arguments......................................................................................................
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cyliner')
parser.add_argument('-r', '--radius', type=int, metavar='', required=True,  help='Radius of Cyliner')
parser.add_argument('-H','--height' type=int, metavar='', required=True, help='Height of Cylinder')
group = parser.add_mutually_exclusive_group()
group.argument ('-q','--quiet', action='store_true', help='print quiet')
group.argument ('-v','--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

def cylinder_volume(radius,height):
    vol = (math.pi) * (radius**2) * (height)
    return vol

if __name__ =='___main___':
    print (cylinder_volume(args.radius,args.height))
    if args.quiet:
        print (volume)
    elif args.verbose:
        print ("Volume of a cylinder with radius {} and height {} is {}".format(args.radius,args.height,volume))
    else:
        print ("volume of Cylinder = {}".format(volume))
        print ("volume of Cylinder = {}".format(volume))


#store_true = the deafult becomes False and when the flag is called it will be given a value of True.
#quiet= prints out one little thing
#verbose is used to print out more information

#run like this:
# python intro_to_argparse.py -r 2 -H 4             Output: Volume of a Cylinder = 50.27
#python intro_to_argparse.py -r 2 -H 4 -q           Output: 50.27
#python intro_to_argparse.py -r 2 -H 4 -v           Output: Volume of a cylinder with radius 2 and height 4 is 50.27


#run: python intro_to_argparse.py -h                if you need help 