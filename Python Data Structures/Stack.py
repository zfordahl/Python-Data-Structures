#Author: Zach Fordahl
#data: 6/4/2024
#description: Use Python stack to show data structure
class stack:
    ######################################
    #            Constructor             #
    ######################################
    def __init__(self):
        self.stack = []

    ####################################
    #          stack size              #
    ####################################
    def size(self):
        counter = -1
        while counter < len(self.stack):
            counter += 1
        return counter

    ####################################
    #              Push                #
    ####################################

    def push(self, data):
        if self.isEmpty() == True:
            print("First index, last to pop => {}".format(data))

        self.stack.append(data)

    ####################################
    #               POP                #
    ####################################
    def pop(self):

        if self.isEmpty() == True:
            print("Stack is Empty")

        else:
            print("Last index, first to pop => {}".format(self.peek()))
            self.stack.pop()

    ####################################
    #          isEmpty                 #
    ####################################
    def isEmpty(self):
        if self.size() == 0:
            return True

    ####################################
    #          Print stack             #
    ####################################

    def printStack(self):
        counter = 0
        print("Stacks are built on => LIFO (last in and first out)")
        for i in self.stack:
            print("{}, Index => {}".format(i, counter))
            counter += 1

    ####################################
    #          Peek top element        #
    ####################################
    def peek(self):
        return self.stack[-1]

    ####################################
    #          Search for item         #
    ####################################

    def search(self, search):
        counter = 0
        for i in self.stack:

            if i == search:
                print("{} found, Index => {}".format(search, counter))

            counter += 1

    def menu(self):
        print(
            "==============>Stack Menu<===============\n1 => Push, 2 => Pop, 3 => Peek, 0 => Exit\n========================================="
        )


####################################
#          Main Class              #
####################################


class main:
    newStack = stack()

    newStack.menu()
    choice = input("Enter choice:")

    while choice != "0":

        if choice == "1":

            inp = input("Enter a push value")
            inp = int(inp)
            newStack.push(inp)
            newStack.printStack()
            newStack.menu()
            choice = input("Enter choice:")

        elif choice == "2":

            newStack.pop()
            newStack.printStack()
            newStack.menu()
            choice = input("Enter choice:")
        elif choice == "3":

            print("Peek value =>{}".format(newStack.peek()))
            newStack.printStack()
            newStack.menu()
            choice = input("Enter choice:")

        else:
            print("Invalid")
            newStack.menu()
            choice = input("Enter choice:")
