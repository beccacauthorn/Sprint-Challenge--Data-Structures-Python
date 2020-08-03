class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        #create the node from the value
        new_node = Node(value)
        #what do we do if tail is none?
        #what's the rule to set to indicate
        #the LinkedList is empty
        #check both head and tail to see if they are empty
        if self.head is None and self.tail is None:
            #both head and tail referring to same node
            self.head = new_node
            self.tail = new_node
        else:
            #these steps assume that the tail is already referring to a node
            #set the old tail's next to refer to the new node
            self.tail.next = new_node
            #reassign self.tail to refer to the new node
            self.tail = new_node 

        self.length += 1

    def remove_head(self):
        #if the linkedlist is empty
        if self.head is None and self.tail is None:
            return
        #only single elem in the linked list
        #then both head and tail are pointing at same node
        if not self.head.next:
            head = self.head
            #delete linked list's head reference
            self.head = None 
            #delete linked list's tail reference
            self.tail = None
            return head.value
        value = self.head.value
        #set self.head to the Node after the head
        self.head = self.head.next

        self.length -= 1
        return value
    
    def remove_tail(self):
        #if there is an empty linked list
        if self.head is None and self.tail is None:
            return None

        #iterate over linked list until the second to last Node
        current = self.head 
        while current is not None and current.get_next() is not self.tail:
            current = current.get_next()

        #current is node right before the tail, set the tail to be none
        # keep the value before deleting it
        value = self.tail.get_value()
        # move self.tail to the node right before
        self.tail = current

        self.length -= 1
        return value 


class RingBuffer:
    def __init__(self, capacity):
        self.list = LinkedList()
        self.capacity = capacity
        self.last_modified = None

    def append(self, item):
        if self.list.length != self.capacity:
            self.list.add_to_tail(item)
            if self.list.length == self.capacity:
                self.list.tail.next = self.list.head
                self.last_modified = self.list.tail
        else:
            self.last_modified.next.value = item
            self.last_modified = self.last_modified.next

    def get(self):
        # put elements in a python list until you see the tail
        elements = []
        current = self.list.head
        while current is not self.list.tail:
            elements.append(current.value)
            current = current.next
        elements.append(self.list.tail.value)
        return elements
