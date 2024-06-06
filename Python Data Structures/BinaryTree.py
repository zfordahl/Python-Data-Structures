"""
Author: Zach Fordahl
date: 5/22/24
description: Binary search tree that arranges words in order 
"""


class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        # Insert Node

        """
   Function that builds the tree. If the value is greater than the root it goes to the right and less then the root to the left. Each iteration checks against the root and the next value in the tree.
    If that value is greater than the current value being checked it gets placed to the right and if less it get placed to the left. 
   """

    def AddToTree(self, data):
        count = 0
        if self.data:

            index = compareDifference(
                data, self.data, count
            )  # will return zero if letters the same and will return index of difference if not

            if compareLeft(data, self.data, index):  # if data < self.data add to left
                print("{} => Left => {}".format(data, self.data))
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.AddToTree(data)

            elif compareRight(
                data, self.data, index
            ):  # if data > self.data add to right
                print("{} <= Right <= {}".format(self.data, data))
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.AddToTree(data)

            else:
                data = self.data

    def menu(self):
        print(
            "==============>BST Menu<========================\n1 => Add, 2 => Traversal, 3 => Search, 0 => Exit\n================================================"
        )

    def PreorderTraversal(self, root):
        Results = []
        if root:
            Results.append(root.data)
            Results = Results + self.PreorderTraversal(root.left)
            Results = Results + self.PreorderTraversal(root.right)
        return Results

    """
  Search will return the target value if found and return none if not. 
  """

    def search(self, root, target):
        if root is None:
            return None
        elif root.data == target:
            return root.data
        elif target < root.data:
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)


########################################################
"""
Key is used to give letters a number value.  Each key(letter) has a corresponding value that represents the value. 
example  letter n would have a value of 14
"""


def alphabetKey(search):
    alpha = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    for keys, value in alpha.items():

        if keys == search:
            return value


########################################################

"""
stringIndex is used to breturn the letter at the corresponding index. example if you had a word of  bacon and you had an index of 2 the returned value would be c. 
stringIndex and aplphabetKey are how the binary tree determines what should be placed left or right  based on the values 
"""


def stringIndex(Word, index):
    count = 0
    if len(Word) > index:
        for w in Word:
            if count == index:
                return w
            count += 1
    else:
        for w in Word:
            if count == (index - 1):
                return w
            count += 1


"""
compare left checks to see if current data is less than previous and returns true if so

"""


def compareLeft(node1, node2, index):

    if alphabetKey(stringIndex(node1, index)) < alphabetKey(stringIndex(node2, index)):
        return True


"""
Compare right checks to see if current data is larger then previous and returns true if so

"""


def compareRight(node1, node2, index):
    if alphabetKey(stringIndex(node1, index)) > alphabetKey(stringIndex(node2, index)):
        return True


def compareDifference(node1, node2, index):

    """The loop will increment the index until there is a difference between the two letters it is comparing. Example zac and zak it would loop on the z and the a but then it gets to the c / k it would stop with
    an index of 2"""

    while (
        alphabetKey(stringIndex(node1, index)) == alphabetKey(stringIndex(node2, index))
        and len(node1) > index
        and len(node2) > index
    ):
        index += 1

    return index


"""
string size checks if the nodes are the same size or different and returns true if the same and false if different. 
"""


def stringSize(node1, node2):
    if len(node1) != len(node2):
        return False
    else:
        return True


class main:

    r = input("Enter the root")

    root = BinaryTree(r.lower())

    root.menu()
    choice = input("Enter choice:")

    while choice != "0":

        if choice == "1":

            inp = input("Enter a String value")
            root.AddToTree(inp.lower())
            choice = input("Enter choice:")

        elif choice == "2":

            print(root.PreorderTraversal(root))
            choice = input("Enter choice:")

        elif choice == "3":
            inp = input("Enter a String value to search")
            print(root.search(root, inp.lower()))
            choice = input("Enter choice:")

        else:
            print("Invalid")
            root.menu()
            choice = input("Enter choice:")