class LinkedListNode:
    """
    A single Node of the LinkedList
    """
    value = None
    next_node = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "<Node data: %s>" % self.value


class LinkedList:
    """
    LinkedList Data Structure
    """

    head = None
    tail = None

    def is_empty(self, value):
        return self.head == True

    def size(self):
        current_node = self.head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.next_node
        return counter

    def add(self, value):
        new_node = LinkedListNode(value)
        if(self.head is None):
            self.head = new_node
        else:
            if self.head.next_node == None:
                new_node.next_node = self.head
                self.tail = self.head
                self.head = new_node
            else:
                new_node.next_node = self.head
                self.head = new_node

    def __repr__(self):
        str = ""
        current_node = self.head
        while current_node:
            if(current_node == self.head):
                str += "[Head: %s] ->" % current_node.value
            elif current_node.next_node == None:
                str += " [Tail: %s]" % current_node.value
            else:
                str += " [%s] ->" % current_node.value
            current_node = current_node.next_node
        return str
