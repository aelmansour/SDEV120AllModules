Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> number_list = list(range(1, 16))
... for number in number_list:
...     if number % 2 == 0:
...         print(f"{number} is even")
...     else:
...         print(f"{number} is odd")
...         
SyntaxError: multiple statements found while compiling a single statement
