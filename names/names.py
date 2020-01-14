import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Big O: O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# -- -- --MY CODE -- -- -- #
# -- -- --MY CODE -- -- -- #

# -!- Data Structures -!-
# 1. BST Class

# -!- Helper Functions -!-
# 1. BST.insert()
# 2. BST.contains()

# -!- Pseudo -!-
# 1. put all names from names_1 into Binary Search Tree => call BST.insert() with all names
# 2. Loop through names_2
#     a. call BST.contains() methon on root tree
#     b. if true
#         - push to duplicated

class BST:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        output = f'Value: {self.value} \n '
        output += f'Left: {self.left} \n '
        output += f'Right: {self.right}'

        return output

    def insert(self, value):
        # Empty Tree
        if self.value == None:
            print('Empty Tree!')
            # DONT MAKE A NEW TREE .. just update this currently empty tree value
            self.value = value

        # > 
        if self.value > value:
            # GO LEFT
            if self.left == None:
                self.left = BST(value)
                print(self.left)
            else:
                self.left.insert(value)


        # <
        if self.value < value:
            # GO RIGHT
            if self.right == None:
                self.right = BST(value)
                print(self.right)
            else:
                self.right.insert(value)
    
    def contains(self, value):
        # Empty Tree
        if self.value == None:
            print('Empty Tree!')
            return False

        # Base Case
        if self.value == value: 
            return True

        # >
        if self.value > value:
            # GO LEFT
            if self.left == None:
                # Value is NOT in BST
                return False
            else: 
                return self.left.contains(value)
        # <
        if self.value < value:
            # GO RIGHT
            if self.right == None:
                # Value is NOT in the BEST
                return False
            else: 
                return self.right.contains(value)

# Create BST
names_tree = BST()

# Fill BST with main array (names_1)
for name in names_1:
    names_tree.insert(name)

# Loop through and check if BST contains any names in check array (names_2)
for name_2 in names_2:
    if names_tree.contains(name_2):
        duplicates.append(name_2)

# -- -- --EMD MY CODE -- -- -- #
# -- -- --EMD MY CODE -- -- -- #

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
