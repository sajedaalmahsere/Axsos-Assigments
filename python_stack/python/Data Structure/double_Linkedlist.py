class Node:
    def __int__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Double_LinkedList:
    def __int__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node =  Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return self
        while current.next != None:
            