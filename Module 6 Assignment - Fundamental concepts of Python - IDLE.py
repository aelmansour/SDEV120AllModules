Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> Print ("Hello World")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Print ("Hello World")
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print ("Hello World")
Hello World
>>> print ("I just wrote my first Python Program")
I just wrote my first Python Program
>>> print ("This is so much fun")
This is so much fun
>>> 
================================ RESTART: Shell ================================
>>> # Variables declarations
>>> c = "cats."
>>> d = "dogs."
>>> # Constructing the sentence using the variables
>>> s = "It is raining " +c[ : -1] + " and + d
SyntaxError: unterminated string literal (detected at line 1)
>>> s = "It is raining " +c[ :-1] + " and " + d
>>> print (s)
It is raining cats and dogs.
