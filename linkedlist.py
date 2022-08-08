class Node:
    def __init__(self, data):
        self.data = data
        self.next = None         # acts as pointer

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # add node at tail
    def append(self, data):
        new_node = Node(data)
        if self.head is None:     # head/tail = node if empty
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:                           # otherwise
            self.tail.next = self.tail  # prev tail node point to new node
            self.tail = new_node        # tail = new node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head.next = self.head
            self.head = new_node
            self.length += 1

    #def insert(self, position, data):









    def print_list(self):
        if self.head is None:
            print("List empty")
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node.next = current_node

ll = LinkedList()
ll.append("bella")
ll.prepend("mama")
ll.print_list()
