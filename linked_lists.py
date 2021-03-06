class Node:
    """
    An object for storing a single node in a linked list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    """
    Singly linked list
    """
    head = None

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds a new node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion takes O(n) time
        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)
        elif index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Return the node or Noneif the key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def removeIndex(self, index):
        """
        Removes node at given index
        """
        current_node = self.head
        previous = None
        deleted_node = None
        last_index = self.size() - 1 

        if index < 0 or index > self.size() - 1:
            print("Index out of range of the list!")
            return None
        else:
            if index == 0:
                deleted_node = self.head
                self.head = current_node.next_node
            elif index == last_index:
                while index > 1:
                    current_node = current_node.next_node
                    index -= 1
                deleted_node = current_node.next_node
                current_node.next_node = None
            else:
                while index > 0:
                    previous = current_node
                    current_node = current_node.next_node
                    index -= 1
                deleted_node = current_node
                previous.next_node = current_node.next_node
        return deleted_node
    
    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return "-> ".join(nodes)
    
