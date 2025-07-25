# Detect and remove loop in a llist
# Linked List helps manage a collection of items
# in a linear, sequential manner
#  Implemented using a Node class
class Node:
    def __init__ (self, data):
        self.data= data
        self.next= None
    # __init__ method initializes objects of the Node class
    #  __str__ method returns a string representation of the Node object
    def __str__(self):
        return str(self.data)
#  __repr__ method returns a string representation of the Node objecct but difference between __str__ and __repr__ is that 
# __repr__ is meant to provide a more detailed representation 
    def __repr__(self):
        return f"Node({self.data})"
    
# LinkedList class manages the collection of Node objects
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def empty(self):
        return self.head is None
    
    def append(self,data):
        new_node = Node(data)
        if self.empty():
            self.head= new_node
            self.tail= new_node
        else:
            current=self.head
            while current.next: # type: ignore
                current = current.next # type: ignore
            current.next = new_node # type: ignore
            self.tail = new_node
    def travese(self):
        current = self.head
        while current:
            print(current, end=" -> ")
            current = current.next
    def inserting_at_beginning(self,data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail= new_node
        else:
            new_node.next = self.head # type: ignore
            self.tail= self.head
            self.head = new_node
    def remove_element(self,data):
        if self.empty():
            return
        if self.head.data == data: #type: ignore
            self.head = self.head.next #type: ignore
            return
        current= self.head.next # type: ignore
        while current: # type: ignore
            print(current.data)
            if current.next.next is None and current.next.data == data: # type: ignore
                current.next = None # type: ignore
                return
            if current.data == data:
                current.next = current.next.next # type: ignore
                return
            current = current.next # type: ignore
    def add_cycle(self, pos):
        if self.empty():
            return
        index = 1
        current = self.head
        cycle = None
        while current.next: # type: ignore
            current = current.next # type: ignore
            if index == pos:
                cycle = current
            index += 1
        tail = current
        tail.next = cycle  # Create a cycle by linking the tail to the node at position 'pos' # type: ignore

        
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
    def remove_loop(self):
        if self.detect_loop():
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next # type: ignore
                fast = fast.next.next
                if slow == fast:
                    break
                # Step 2: Loop detected — find the start of the loop
            slow = self.head
            if slow == fast:
                # Special case: loop starts at head, because if slow and fast rest at the same node both will start moving together and you will never be able to find cycle case of 1 -> 2 -> 3 -> 4-> 1
                while fast.next != slow: # type: ignore
                    fast = fast.next   # type: ignore
            else:
                while slow.next != fast.next: # type: ignore
                    slow = slow.next # type: ignore
                    fast = fast.next # type: ignore

            # Step 3: Remove the loop
            fast.next = None # type: ignore

ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.add_cycle(2) # Create a cycle for testing
# ll.travese()
# print(ll.detect_loop()) # Should return True
ll.remove_loop()
ll.travese()