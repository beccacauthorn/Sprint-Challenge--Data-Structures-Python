class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def remove_head(self):
        #if the linkedlist is empty
        if self.head is None:
            return
        #only single elem in the linked list
        #then both head and tail are pointing at same node
        if not self.head.get_next():
            head = self.head
            #delete linked list's head reference
            self.head = None
            return head.get_value()
        value = self.head.get_value()
        #set self.head to the Node after the head
        self.head = self.head.get_next()
        return value

    def reverse_list(self, node, prev):
        stack = Stack()
        current = self.head
        while current is not None:
            stack.push(current.get_value())
            current = current.get_next()

        self.head = stack.storage.head


class Stack:
    def __init__(self):
        self.size = 0 
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        return None
   

