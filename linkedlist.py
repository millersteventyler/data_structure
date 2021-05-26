from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temporary_node = self.head
        while temporary_node.next is not None:
            temporary_node = temporary_node.next
        temporary_node.next = node

    def add_to_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def contains_node(self, search):
        current = self.head
        while current is not None:
            if current.data == search:
                return True
            current = current.next
        return False
