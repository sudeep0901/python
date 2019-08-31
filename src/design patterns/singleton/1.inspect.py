import inspect
import dis


class SampleClass:
    """Definition for X class."""
    def __init__(self, name, *args, **kwargs):
        self.name = name

    def get_name(self):
        "Returns the name of the instance."
        return self.name

x = SampleClass("sudeep Patel")

x.name = "Sudeep Patel"


def module_funct(arg1, arg2 = 'default', *args):
    """This is a module-level function."""
    local_var = arg1 * 3
    return local_var


for key, data in inspect.getmembers(SampleClass, inspect.isfunction):
    print('{} : {!r}'.format(key, data))

for key, data in inspect.getmembers(SampleClass, inspect.ismethod):
    print('{} : {!r}'.format(key, data))

print(inspect.getdoc(x))

print(inspect.getsource(SampleClass))

print(dis.dis(module_funct))