"""
Queue are linear data structures that store items in FIFO order. This means the item that is added to the queue first is the first to be removed when removing an item.
They work on a big O(1) when adding to the stack and removing. They are extremely effective for holding a large amout of data in order when you don't know the size of how much is going to be needed to be held
and when items needed to be added and removed very quickly.

Author: Zach Fordahl
Date: 5/21/24
Description: Show how Queues work. 
"""


class queue:
    ######################################
    #            Constructor             #
    ######################################
    def __init__(self):
        self.queue = []

    ####################################
    #         queue  size              #
    ####################################
    def size(self):
        counter = -1
        while counter < len(self.queue):
            counter += 1
        return counter

    ####################################
    #           enqueue                #
    ####################################

    def enqueue(self, data):
        if self.isEmpty() == True:
            print("First index, first to Dequeue => {}".format(data))

        self.queue.append(data)

    ####################################
    #              dequeue             #
    ####################################
    def dequeue(self):

        if self.isEmpty() == True:
            print("Queue is Empty")

        else:
            print("Last index, last to Dequeue => {}".format(self.peek()))
            self.queue.pop(0)

    ####################################
    #          isEmpty                 #
    ####################################
    def isEmpty(self):
        if self.size() == 0:
            return True

    ####################################
    #          Print queue             #
    ####################################

    def printQueue(self):
        counter = 0
        print("Queue are built on => FIFO (First In First Out)")
        for i in self.queue:
            print("{}, Index => {}".format(i, counter))
            counter += 1

    ####################################
    #          Peek Bottom element     #
    ####################################
    def peek(self):
        return self.queue[0]

    ####################################
    #          Search for item         #
    ####################################

    def search(self, search):
        counter = 0
        for i in self.queue:

            if i == search:
                print("{} found, Index => {}".format(search, counter))

            counter += 1

    def menu(self):
        print(
            "===================>Queue Menu<=================\n1 => Enqueue, 2 => Dequeue, 3 => Peek, 0 => Exit\n================================================"
        )


####################################
#          Main Class              #
####################################


class main:
    newQueue = queue()

    newQueue.menu()
    choice = input("Enter choice:")

    while choice != "0":

        if choice == "1":

            inp = input("Enter a push value")
            inp = int(inp)
            newQueue.enqueue(inp)
            newQueue.printQueue()
            newQueue.menu()
            choice = input("Enter choice:")

        elif choice == "2":

            newQueue.dequeue()
            newQueue.printQueue()
            newQueue.menu()
            choice = input("Enter choice:")
        elif choice == "3":

            print("Peek value =>{}".format(newQueue.peek()))
            newQueue.printQueue()
            newQueue.menu()
            choice = input("Enter choice:")

        else:
            print("Invalid")
            newQueue.menu()
            choice = input("Enter choice:")
