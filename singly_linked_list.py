class node:
    def __init__(self, data = None):
        self.data = data  # here we'll be storing the passed data point
        self.next = None  # this we'll be storing the pointer to the next node, in the constructor we initialize to None
        # the last element in the linked list is going to have it's pointer set to None
        # if a child is going to be attached to this node than we'll be updating this (self.next) variable


class linked_list:
    """ This ia a wrapper that interfaces over the nodes, the user is not going to interact with the nodes directly
        this is a subclass of the Node.
    """
    
    def __init__(self):
        """ In the constructor we'll always going to have the head node inside the linked list, the head node is not
        going to contain any actual data is not going to be indexable (the user isn't going to be able able to access
        this head not, this is going to be used a placeholder to allow as to allow us to point to the first element
        of the list, when we're first creating out list we're going to have a list of length zero.
        """
        self.head = node()
    
    def append(self, data):
        """ This function is going to be adding a node to the end of the current list """
        new_node = node(data)
        current = self.head  # we're starting at the left most point in the list
        while current.next is not None:  # we're iterating over each element of the list starting with the head
            current = current.next
        current.next = new_node
    
    def length(self):
        """ Returning the length of the linked list """
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total
    
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
    
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1
    
    def erase(self, index):
        if index >= self.length():
            print("Error 'Erase' Index out of range!")
            return
        
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


my_list = linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.display()
print(f'Element at 1st index : {my_list.get(1)}')
my_list.erase(1)
my_list.display()
