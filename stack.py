# stack implemented w linked list

class Node:
    def __init__(self, data): # pass data when instance is created
        self.data = data
        self.next = None # acts as pointer to next node

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def peek(self):
        if self.top != None: return self.top.data
            
    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top  # cur node point to new node 
            self.top = new_node       # this adds to top of stack
        self.length += 1

    def pop(self):
        if self.top == None:
            print("Stack empty")
        else:
            self.top = self.top.next  # top = pointed/prev node (removes top)
            self.length -= 1
            if self.length == 0:
                self.top = None # programme understands stack is empty (line26)

    def print_stack(self):
        if self.top == None:
            print("Stack empty")
        else:
            #create placeholder var so below code doesn't remove real stack
            current_node = self.top 
            while current_node != None:       #loop until bottom
                print(current_node.data)          #print top
                current_node = current_node.next  #top = previous node
                                                  #act as pop() to go down stack
stack = Stack()

stack.push("bella")
stack.push("bell0")
stack.push("stack")
stack.push("mama")
stack.pop()
stack.pop()
stack.print_stack()
