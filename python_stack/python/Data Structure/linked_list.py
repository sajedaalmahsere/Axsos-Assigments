class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_start(self, value):
        new_node = Node(value)  #variable I used to add a new node
        if self.head == None:
            self.head = new_node
            return self
        #step1: new_node next should be the currrent head
        new_node.next = self.head
        #step2: make the new node into the head of the linked list
        self.head = new_node
        return self

    def add_to_tail(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return self
        current =  self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        return self

    
