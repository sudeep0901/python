class FrozenAttr:
    def __init__(self, mapping):
        print("FrozenAttr called")
        self.__data = dict(mapping)
    

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            getattr(self.__data, name)
        
        else: 
            return self.__data[name]
                

