class MyQueue:

    def __init__(self):
        self.my_arr = []

    def push(self, x: int) -> None:
        self.my_arr.append(x)

    def pop(self) -> int:
        pop_val = self.my_arr[0]
        self.my_arr = self.my_arr[1:]
        return pop_val

    def peek(self) -> int:
        return self.my_arr[0]

    def empty(self) -> bool:
        if len(self.my_arr) > 0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()