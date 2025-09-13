class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        result = self.map.get(key)
        if result is None:
            result = -1
        return result

    def remove(self, key: int) -> None:
        result = self.map.pop(key, -1)
        return result

    def display_values(self):
        print('Printing the key in the map:')
        for key, value in self.map.items():
            print('Key:', key, 'Value:', value)


if __name__ == '__main__':

    my_hash_map = MyHashMap()
    my_hash_map.put(1, 1)
    my_hash_map.display_values()
    print('Removed element:', my_hash_map.remove(1))
    my_hash_map.display_values()
    print('Removed element:', my_hash_map.remove(1))
    my_hash_map.display_values()
