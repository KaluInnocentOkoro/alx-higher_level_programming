#!/usr/bin/python3
""" A Node Class"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiates a singly linked list
        Args:
            data (int): An integer
            next_node (Node) or (None): next node on the lists
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data of a linked list"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of a singly linked list
        Args:
            value (int): An integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves the next node pointer"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the pointer to the next node of the list
        Args:
            value (Node): A node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Method inserts a new node into the correct sorted position
        Args:
            value (int): integer to be added
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Prints the linked list data"""
        vals = []
        temp = self.__head
        while temp is not None:
            vals.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(vals)
