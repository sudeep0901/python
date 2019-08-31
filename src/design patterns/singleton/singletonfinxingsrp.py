# fixing srp issue
# Signleton base class


class Singleton(object):
    _instances = {}  # dict instance

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(cls)
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
