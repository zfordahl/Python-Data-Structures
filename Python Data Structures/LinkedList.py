# Author:Zach Fordahl
# Date: 6/4/24
# descript: Show how linked list gets implemented.
# node class uses constructor to add data and link next.
class node:
    # constructor for node class takes data and next
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


"""
linkedList class includes:
Constructor, Insert- beginning middle and end,
search, and print
"""


class linkedList:
    def __init__(
        self,
    ) -> None:
        self.head = None

    # Create linked list and insert nodes
    def Insert(self, data):
        newNode = node(data)
        # create node object
        if self.head == None:
            self.head = newNode  # create head if empty
        else:

            newNode.next = self.head
            self.head = newNode

    # Adds nodes at the end of the linked list

    def InsertEnd(self, data):
        newNode = node(data)  # create new node object

        if self.head is None:  # check if empty
            self.head = newNode
            return

        tail = self.head  # create reference variable
        while tail.next:  # loop through all elements in var
            tail = tail.next  # once completed all elements.next
        tail.next = newNode  # add new node to end

    # search return if the data exist and at what node it exist at
    def search(self, data):
        count = 1
        current = self.head
        while current:

            if current.data == data:
                print("{} found node{}".format(data, count))
            count += 1
            current = current.next

    # gives size of the linked list
    def linkListSize(self):
        count = 1
        size = self.head
        while size.next:
            count += 1
            size = size.next
        return count

    # gives middle of list
    def LinkedListMiddle(self, size):
        count = 0
        if (size % 2) == 0:
            count = size / 2  # find half if even
        else:
            count = (size + 1) / 2  # find half if odd
        return count

    # Inserts into the middle of linked list. Depending if odd or even will change where element is placed.
    def insertMiddle(self, data):
        newNode = node(data)
        middle = self.head
        count = self.LinkedListMiddle(self.linkListSize())
        size = self.linkListSize()

        if (size % 2) == 0:
            count += 1

        while count < size:
            count += 1
            middle = middle.next
        newNode.next = middle.next
        middle.next = newNode

    # prints list
    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


class main:

    list = linkedList()

    list.Insert("BOB")
    list.Insert("Jon")
    list.Insert("Jon")
    list.Insert("Tyler")
    list.Insert("Tom")
    list.insertMiddle("John")
    list.InsertEnd("jimmy")
    list.printLinkedList()
    list.search("Tim")