# Doubly linked List Implementation
# Linked List helps manage a collection of items
# in a linear, sequential manner
# Implemented using a Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        # __init__ method initializes objects of the Node class

class DoublyLinkedList:
    def __init__ (self):
        self.head=None
        self.tail=None
        # __init__ method initializes objects of the DoublyLinkedList class

    def empty(self):
        return self.head is None
    
    def append(self, data):
        new_Node = Node(data)
        if self.empty():
            self.head = new_Node
        else:
            current = self.head
            while current.next: # type: ignore
                current = current.next # type: ignore
            current.next = new_Node # type: ignore
            new_Node.prev = current # type: ignore

    def traverse(self):
        current = self.head
        while current:
            print(f"{current.data}", end=" <-> ")
            current = current.next
    def reverse_traverse(self):
        current = self.head
        while current:
            current = current.next
        while current:
            print(f"{current.data}", end=" <-> ")
            current = current.prev

    def insert_at_beginning(self, data):
        new_Node = Node(data)
        if self.empty():
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head # type: ignore
            self.head.prev = new_Node # type: ignore
            self.head = new_Node
            self.tail = new_Node
        
    def remove_element(self, data):
        if self.empty():
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next= current.next
                if current.next:
                    current.next.prev= current.prev
                if current == self.head:
                    self.head = current.next

ll = DoublyLinkedList()
ll.append(1)
ll.append(2)
ll.append(5)
ll.append(8)
ll.traverse()
ll.remove_element(5)
ll.traverse()
ll.reverse_traverse