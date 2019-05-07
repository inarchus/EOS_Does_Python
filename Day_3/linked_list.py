class LinkedListNode:
    def __init__(self, value = 0):
        self.next = None
        self.value = value
        

class BSTNode:
    def __init__(self, value=0):
        self.left = None
        self.right = None
        self.value = value


class ConfusoClass:
    x = 1
    
    def __init__(self):
        print(self.x, ConfusoClass.x)
        self.x += 1
        print(self.x, ConfusoClass.x)


a = ConfusoClass()
y = ConfusoClass()

start = LinkedListNode(3)
n2 = LinkedListNode(5)

start.next = n2

print(start.next.value)
