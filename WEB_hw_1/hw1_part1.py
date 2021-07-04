from abc import abstractclassmethod, ABC, ABCMeta
import pickle
import json

class SerializationInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def serialize(self):
        pass

    @abstractclassmethod
    def deserialize(self):
        pass

    
class SerializationListJson(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)


class SerializationTupleJson(SerializationInterface):
    def serialize(self, data):
        return json.dumps(tuple(data))

    def deserialize(self, packed_data):
        return tuple(json.loads(packed_data))

    
class SerializationDictJson(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)


class SerializationSetJson(SerializationInterface):

    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed):
        return set(json.loads(packed))

class SerializationListBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationTupleBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationDictBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class SerializationSetBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


if __name__ == '__main__':
    data_list = [1, 2, 3]
    data_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    data_tuple = (1, 2, 3, 4, 5, 6)
    data_set = {1, 2, 3, 4, 5, 6}
    # 1 serialize  - deserialize json list
    print("#        1 serialize  - deserialize json list")
    packed = SerializationListJson().serialize(data_list)
    print(f'Serialize data - {packed}')
    unpacked = SerializationListJson().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_list == unpacked, 'No correct deserialize json list'
        print(f'SUCCESS: JSON for List: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
    
    # 2 serialize  - deserialize json dict
    print("\n#      2 serialize  - deserialize json dict")
    packed = SerializationDictJson().serialize(data_dict)
    print(f'Serialize data - {packed}')
    unpacked = SerializationDictJson().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_dict == unpacked, 'No correct deserialize json dict'
        print(f'SUCCESS: JSON for Dict: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
        
    # 3 serialize  - deserialize json tuple
    print("\n#      3 serialize  - deserialize json tuple")
    packed = SerializationTupleJson().serialize(data_tuple)
    print(f'Serialize data - {packed}')
    unpacked = SerializationTupleJson().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_tuple == unpacked, 'No correct deserialize json tuple'
        print(f'SUCCESS: JSON for Tuple: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
        
    # 4 serialize  - deserialize json set
    print("\n#       4 serialize  - deserialize json set")
    packed = SerializationSetJson().serialize(data_set)
    print(f'Serialize data - {packed}')
    unpacked = SerializationSetJson().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_set == unpacked, 'No correct deserialize json set'
        print(f'SUCCESS: JSON for Set: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
        
    # 5 serialize  - deserialize bin list
    print("\n        5 serialize  - deserialize bin list")
    packed = SerializationListBin().serialize(data_list)
    print(f'Serialize data - {packed}')
    unpacked = SerializationListBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_list == unpacked, 'No correct deserialize bin list'
        print(f'SUCCESS: BIN for List: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
        
    # 6  serialize  - deserialize bin dict
    print("\n#      6  serialize  - deserialize bin dict")
    packed = SerializationDictBin().serialize(data_dict)
    print(f'Serialize data - {packed}')
    unpacked = SerializationDictBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_dict == unpacked, 'No correct deserialize json dict'
        print(f'SUCCESS: BIN for Dict: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
        
    # 7 serialize  - deserialize bin tuple
    print("\n#       7 serialize  - deserialize bin tuple")
    packed = SerializationTupleBin().serialize(data_tuple)
    print(f'Serialize data - {packed}')
    unpacked = SerializationTupleBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_tuple == unpacked, 'No correct deserialize json tuple'
        print(f'SUCCESS: BIN for Tuple: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
        
    # 8 serialize  - deserialize bin set
    print("\n#       8 serialize  - deserialize bin set")
    packed = SerializationSetBin().serialize(data_set)
    print(f'Serialize data - {packed}')
    unpacked = SerializationSetBin().deserialize(packed)
    print(f'Deserialize data - {unpacked}')
    try:
        assert data_set == unpacked, 'No correct deserialize json set'
        print(f'SUCCESS: BIN for Set: {unpacked}')
    except AssertionError as error:
        print(f'\n{error}\n')
    



