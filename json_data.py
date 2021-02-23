import json
from collections import abc
with open('data.txt', 'rb') as f:
    datajson = json.load(f)
print(datajson)
class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)  

    def __getattr__(self, name):  
        if hasattr(self.__data, name):
            print(name)
            return getattr(self.__data, name)  
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):  
        if isinstance(obj, abc.Mapping):  
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):  
            return [cls.build(item) for item in obj]
        else:  
            return obj

data = FrozenJSON(datajson)
print(data)

class GetListObject:
    def __init__(self, ref):
        self.__ref = ref
    def __getattr__(self, name):
        print('getlist', name)
        return [getattr(x, name) for x in self.__ref]
    def __getitem__(self, key):
        print('getitem', key)
        return self.__ref[key]

class GetObject:
    def __init__(self, ref):
        self.__ref = ref
    def __getattr__(self, name):
            print('get', name)
            if hasattr(self.__ref, name):
                print('hasattr', name)
                print('build', type(self.__ref), isinstance(self.__ref, abc.MutableSequence), self.__ref.keys())
                obj = getattr(self.__ref, name)
                if isinstance(obj, abc.MutableSequence):
                    print('-------', [GetObject(item) for item in obj])
                    return GetListObject(obj)
                else:
                    obj = getattr(self.__ref, name)
                    print('build-----', type(obj), isinstance(obj, abc.MutableSequence))
                    if isinstance(obj, str):
                        return obj
                    else:
                        return GetObject(obj)
            else:
                return self.__ref

