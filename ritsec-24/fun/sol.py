import ast

# Running the file doesn't result in the right array???

"""
author:
i think this is an error on my end, Node Transformer casted the None as an int (on purpose), dumping it to python code removed the cast
i know of others that have managed to solve it still, will provide a slight hint since this is a mistake with my obfuscator.
assume each None is an int and that should be a valid workaround
you can also just check which one doesnt call another function
"""

with open('clean.py', 'r') as f:
    source = f.read()


print(ast.dump(ast.parse(source, mode='exec')))
