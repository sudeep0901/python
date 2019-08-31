
some_guy = 'Fred'

first_names = []
first_names.append(some_guy)

another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print(some_guy, first_names, another_list_of_names)


class callableObject():
    def __init__(self):
        print('__init called')
       

    def __call__(self):
        print("I am callableobject")

    def __add__(self):
        print("Add called")
    


cob = callableObject()

# cob()
print(dir(cob))
