print("task1")
print("hello World")
print(123)
print(43.1)
print(3+2j)
print("hello")
print(True)


print(int(123),type(123),sep='is type of')
print(float(43.23),type(43.23),sep='is type of')
print(complex(4-1j),type(4-1),sep='is type of')
print(str ('How Are You?'),type('How Are You'))
print(bool('true'),type (bool('true')),sep='is type of')


print(isinstance(123,int))
print(isinstance(43.23,str))
print(isinstance(True,bool))
print(isinstance(4-1j,complex))
print(isinstance('city',int))

print('Is 123  an instance of int?:', isinstance(123,int))
print('Is 43.23  an instance of bool?:', isinstance(43.23,bool))
print('Is (4-1j)  an instance of complex?:', isinstance(4-1j,complex))
print('Is True  an instance of bool?:', isinstance('True',bool))
print('Is "How Are You?"  an instance of float?:',isinstance('How are you?',float))

# This is my first comment
# Block comments are indented to the same level as that code
print("Hello")
print("Line with inline code!")
print(type(123.45))
"""You can use triple-quoted strings. When they're not a docstring (the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!"""