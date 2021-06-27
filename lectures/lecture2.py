Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 2**4000
13182040934309431001038897942365913631840191610932727690928034502417569281128344551079752123172122033140940756480716823038446817694240581281731062452512184038544674444386888956328970642771993930036586552924249514488832183389415832375620009284922608946111038578754077913265440918583125586050431647284603636490823850007826811672468900210689104488089485347192152708820119765006125944858397761874669301278745233504796586994514054435217053803732703240283400815926169348364799472716094576894007243168662568886603065832486830606125017643356469732407252874567217733694824236675323341755681839221954693820456072020253884371226826844858636194212875139566587445390068014747975813971748114770439248826688667129237954128555841874460665729630492658600179338272579110020881228767361200603478973120168893997574353727653998969223092798255701666067972698906236921628764772837915526086464389161570534616956703744840502975279094087587298968423516531626090898389351449020056851221079048966718878943309232071978575639877208621237040940126912767610658141079378758043403611425454744180577150855204937163460902512732551260539639221457005977247266676344018155647509515396711351487546062479444592779055555421362722504575706910949376
>>> 
>>> 2.0**4000
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    2.0**4000
OverflowError: (34, 'Result too large')
>>> 0.5 - 0.25
0.25
>>> 0.3 - 0.1
0.19999999999999998
>>> 10+2
12
>>> 10+2+
SyntaxError: invalid syntax
>>> 10/0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
>>> 10+2)
SyntaxError: invalid syntax
>>> (10+2
 -2)
10
>>> #*,/,+,-
>>> 3/2
1.5
>>> 4/2
2.0
>>> 3//2
1
>>> 4//2
2
>>> //
SyntaxError: invalid syntax
>>> //
SyntaxError: invalid syntax
>>> //
SyntaxError: invalid syntax
>>> 4 // 2
2
>>> 4 % 2
0
>>> 4 % 3
1
>>> 11 % 4
3
>>> 11 // 4
2
>>> #4 in 11
>>> #7
>>> #3
>>> 
>>> 2 < 3
True
>>>  2<3
 
SyntaxError: unexpected indent
>>> 2 <= 2
True
>>> 2 = 2
SyntaxError: can't assign to literal
>>> 2 == 2
True
>>> 2==3
False
>>> 2+2 < 45
True
>>> 2 + (2 < 45)
3
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

>>> round(3.2)
3
>>> round(3.5)
4
>>> round(3.17336832632818262, 2)
3.17
>>> round(3.1790827310, 2)
3.18
>>> round(0.3-0.1, 6)
0.2
>>> max(2,10,-3.5,100.2)
100.2
>>> print("bdyibdqibdi")
bdyibdqibdi
>>> print("hellow")
hellow
>>> 2 ! -2
SyntaxError: invalid syntax
>>> 2!=2
False
>>> abs(-8.6)
8.6
>>> area_of_triangle(4,2)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    area_of_triangle(4,2)
NameError: name 'area_of_triangle' is not defined
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> x=2.5
>>> print(x)
2.5
>>> x=2
>>> print(x)
2
>>> x
2
>>> type(3.7)
<class 'float'>
>>> type(x)
<class 'int'>
>>> x=true
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    x=true
NameError: name 'true' is not defined
>>> x=True
>>> type(x)
<class 'bool'>
>>> x=4
>>> counter= 3 * x
>>> x
4
>>> counter
12
>>> x
4
>>> x=1
>>> counter
12
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x=4
>>> counter = 3*x
>>> x=1
>>> area_of_triangle(4,2)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    area_of_triangle(4,2)
NameError: name 'area_of_triangle' is not defined
>>> def area_of_triangle(base, height):
	area=base*height/2
	return area

>>> area_of_triangle(4,2)
4.0
>>> 
