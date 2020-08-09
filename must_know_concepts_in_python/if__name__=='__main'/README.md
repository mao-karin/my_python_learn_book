# if__name__=="__main__" tutorial


Background on __main__
-----------------------
Watch this video to understand: https://www.youtube.com/watch?v=pzNISmtmzcY

__main__ is the starting point of execution. First module's name. It changes with the script.


Concept of if __name__=="__main__"
----------------------------------
`__main__` is the name of the scope in which top-level code executes. A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.

A module can discover whether or not it is running in the main scope by checking its own __name__, which allows a common idiom for conditionally executing code in a module when it is run as a script or with python -m but not when it is imported:

    if__name__=="__main__":
        #executes only if run as a script 
        main()

For a package, the same effect can be achieved by including a __main__.py module, the contents of which will be executed when the module is run with -m.


Why do we need it?
------------------
myfunc.py

    def add (a,b):
        return (a + b)
    
    print add(2,3)

test.py

    from myfunc import add
    
    print add(2,2)

So, if you run myfunc.py it will output 5.
If you run test.py it will output 5 then 4.

so this is where you want to use __name__ == “main”.

myfunc.py

    def add (a,b):
        return (a + b)
    
    if__name__=="__main__":
        print add(2,3)

test.py

    from myfunc import add
    
    print add(2,2)

So, if you run test.py, output is 4.

The __main__ is no longer executed because the __name__ is no longer "__main__". Now the __name__ = myfunc. You can check this by print __name__.


Notes:

- if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported. if imported and called in another script, if __name__=="__main__" will - not execute.

- You can test whether your script is being run directly or being imported by something else by testing __name__ variable.

- If script is getting imported by some other module at that time __name__ will be module name.


Some useful links:

https://www.youtube.com/watch?v=JtKOP-ThcbU
