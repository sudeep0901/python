class Foo(object):

    def instance_method(self, arg):
        print("I am instance method", self, arg)
    
    @classmethod
    def class_method(cls, arg):
        print("class method", arg)
        print(cls, dir(cls))
    
    @staticmethod    
    def static_method(arg):
        print("static method", arg)


foo = Foo()

foo.instance_method("Hello")

foo.class_method("classmethod")
foo.static_method("static methods")

Foo.class_method("I am class method")

umeth = Foo.instance_method
umeth("Hello", 37)

f = Foo()

umeth(f, 37)
umeth(str, 37)

print(type(umeth))

print(umeth.__name__,
      umeth.__class__,
#       umeth.__func__,
#       umeth.__self__
      )

