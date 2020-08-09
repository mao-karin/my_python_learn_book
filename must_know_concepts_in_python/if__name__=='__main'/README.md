# Python Argparse Tutorial

Python's `argparse` module makes it easy to write user-friendly command-line interfaces. It is the recommended command-line parsing module in the Python standard library.

This folder holds files related to `argparse` tutorial. Files that helped me learn so wanted to share it with anyone starting out.
The argparse tutorial documentation for python can be found here: [ArgparseTutorial] (https://docs.python.org/3/howto/argparse.html)


Installation
------------
`argparse` is part of Python's standard library, meaning you don't need to install anything apart from a basic Python environment!


Basics
------
Command-line arguments are passed to Python programs via `sys.argv`:

    import sys
    print(sys.argv)

The `argparse` module provides a mechanism to define the arguments a program requires and takes care of parsing those out of sys.argv.  

Let's start with a the format:

    import argparse
    parser = argparse.ArgumentParser()                                        #create the parser
    parser.add_argument('input', type=int, help='input here' )                #add argument(s)
    args= parser.parse_args()                                                 #execute the parse_args() method

    print(args.input)                                                         #use the parser argument in your code 


Positional arguments
--------------------
The first type of arguments `argparse` can parse are positional arguments.
They derive their name from the fact that a program should know what to do
with the arguments based solely on where it appears on the command line.

An example:

    import argparse
    parser = argparse.ArgumentParser(description='Create a new FITS file '
                                                 'containing one extension '
                                                 'from an existing FITS file.')
    parser.add_argument('filename',
                        help='path to a FITS file')
    parser.add_argument('extension', type=int,
                        help='the FITS extension number')
    args = parser.parse_args()
    print(args.filename)


Optional arguments
------------------
Optional arguments allow the user to change behaviour of a program using optional flags or parameters.

An example:

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase verbosity')
    args = parser.parse_args()
    if args.verbosity:
        print('verbose turned on')


Advanced contents of the tutorial
---------------------------------
- Adding [mutually exclusive arguments](example-scripts/fitsextract3.py#L19)


Futher reading
--------------
* [A comparison of different command-line parsing libraries](https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
