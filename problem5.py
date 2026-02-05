class MyHashMap:

    def __init__(self):
        self.key_arr = []
        self.val_arr = []

    def put(self, key: int, value: int) -> None:
        if key in self.key_arr:
            index_val = self.key_arr.index(key)
            self.val_arr[index_val]=value
        else:
            self.key_arr.append(key)
            self.val_arr.append(value)

    def get(self, key: int) -> int:
        if key in self.key_arr:
            index_val = self.key_arr.index(key)
            return self.val_arr[index_val]
        return -1

    def remove(self, key: int) -> None:
        if key in self.key_arr:
            index_val = self.key_arr.index(key)
            self.key_arr = self.key_arr[:index_val]+self.key_arr[index_val+1:]
            self.val_arr = self.val_arr[:index_val]+self.val_arr[index_val+1:]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)