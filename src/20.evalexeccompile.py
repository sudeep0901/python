a = [3, 5, 10, 13]
exec("for i in a: print(i)")

res = eval('2 + 2')

globals = {'x': 7,
           'y': 10,
           'birds': ['Parrot', 'Swallow', 'Albatross']
           }
locals = {}
# Execute using the above dictionaries as the global and local namespace
a = eval("3 * x + 4 * y", globals, locals)
exec("for b in birds: print(b)", globals, locals)
# When a string is passed to exec() or eval() the parser first compiles it into bytecode.
# Because this process is expensive, it may be better to precompile the code and
# reuse the bytecode on subsequent calls if the code will be executed multiple times.
s = "for i in range(0,10): print(i)"
c = compile(s,'','exec') # Compile into a code object
exec(c) # Execute it
# s2 = "3 * x + 4 * y"
# c2 = compile(s2, '', 'eval') # Compile into an expression
# result = eval(c2) # Execute it
