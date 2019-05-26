class Vector:
    # def __init__(self, x, y):
    #     print("Object init method called")
    #     self.x = x
    #     self.y = y

    # def __init__(self, **coords):
    #     print("Object init method called")

    #     self.__dict__.update(coords)
    # when prefix with underscode, object attributes are private 
    # and cannot be accessed from class instance directly
    # when accessing attribute starting with _, AttributeError is reaised
    def __getattr__(self, name):
        print("name=",name)
        private_name = "_" + name
        if private_name not in self.__dict__:
            raise(AttributeError("object has notatribute {!r}".format(private_name)))
        return getattr(self, private_name)

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attr {!r}".format(name))
        
    def __init__(self, **coords):
        print("Object init method called")
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)


    def __repr__(self):
        # return "{} {}, {}".format(
        #     self.__class__, self.x, self.y)
        return "{}, {}".format(
            self.__class__.__name__,
            ", ".join("{k}={v}".format(
                k=k, v=self.__dict__[k])
                for k in sorted(self.__dict__.keys()
                                )
            )
        )


# can access diction ary object using 
# vars(object name)
# object.__dict__