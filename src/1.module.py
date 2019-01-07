import initcalllmethods

print(initcalllmethods.__dict__)
print(initcalllmethods.__name__)
print(initcalllmethods.__file__)
 
f = initcalllmethods.Foo("x", "y", "z")

print(f.__dict__)
