 # metaclass
# fixing srp issue
# Signleton base class
class Singleton(type):
    _instances = {} # dict instance

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(cls)
            instance = super().__call__(*args,*kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

