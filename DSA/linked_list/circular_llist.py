class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head #type: ignore
        else:
            current = self.head
            while current.next != self.head: #type: ignore
                current = current.next #type: ignore
            current.next = new_node #type: ignore
            new_node.next=self.head #type: ignore
    def traverse(self):
        if self.head is None:
            return 
        if self.head.next == self.head:
            print(self.head.data)
            return
        current = self.head
        while current.next !=self.head: #type: ignore
            print (current.data) #type: ignore
            current = current.next #type: ignore
        print(current.data)  #type: ignore 
    def delete(self , key):
        if self.head is None:
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
                return
            else:
                current = self.head
                while current.next != self.head: #type: ignore
                    current = current.next #type: ignore
                current.next = self.head.next #type: ignore
                self.head = self.head.next #type: ignore
        else:
            current = self.head
            while current.next != self.head and current.next.data != key: #type: ignore
                current = current.next #type: ignore
            if current.next.data == key: #type: ignore
                current.next = current.next.next #type: ignore
            else:
                print("Key not found in the list")
    
ll= CircularLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.traverse()
ll.delete(3)
ll.traverse()
ll.delete(1)
ll.traverse()