
class Meta(type):
    
    def __new__(cls, future_class_name, future_class_parents, future_class_atrrs):
        future_class_atrrs['class_number'] = Meta.children_number
        Meta.children_number += 1
        return type(future_class_name, future_class_parents, future_class_atrrs)
 

Meta.children_number = 0

class Cls1(metaclass=Meta):

    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):

    def __init__(self, data):
        self.data = data
        

class Cls3(metaclass=Meta):

    def __init__(self, data):
        self.data = data

        
print(Cls1.class_number, Cls2.class_number, Cls3.class_number)
assert (Cls1.class_number, Cls2.class_number, Cls3.class_number) == (0, 1, 2)
a, b, c = Cls1(''), Cls2(''), Cls3('')
print(a.class_number, b.class_number, c.class_number)
print(Meta.children_number)
assert (a.class_number, b.class_number, c.class_number) == (0, 1, 2)
