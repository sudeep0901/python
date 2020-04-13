class Class:
    # by default below are class attributes
    data = 'the class data attr'

    @property
    def prop(self):
        return 'the prop value'



# Class Attribute
obj = Class()
print(Class.__dict__)
vars(Class)
vars(obj)

print(obj.data)
print(obj.prop)

# cannot set prop from obj

try:
    obj.prop = "setting class prper value"
except AttributeError:
    print('cannot set property as readonly')


# setting values using instance
# Writing to obj.data creates an instance attribute.
obj.data = "new value"
print(vars(obj))

# class variable unchanged
# Now reading from obj.data retrieves the value of the instance attribute. When
# read from the obj instance, the instance data shadows the class data .
print(Class.data)

# Reading prop directly from Class retrieves the property object itself, without
# running its getter method.
# Reading obj.prop executes the property getter.
# Trying to set an instance prop attribute fails.
# Putting 'prop' directly in the obj.__dict__ works.
# We can see that obj now has two instance attributes: attr and prop .
# However, reading obj.prop still runs the property getter. The property is not
# shadowed by an instance attribute.
# Overwriting Class.prop destroys the property object.
# Now obj.prop retrieves the instance attribute. Class.prop is not a property
# anymore, so it no longer overrides obj.prop .

obj.__dict__['prop'] = 'foo'
print(vars(obj))
Class.prop  = 'class propert changes'
print(vars(Class))











