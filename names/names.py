import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# -- -- --MY CODE -- -- -- #
# -- -- --MY CODE -- -- -- #

# -!- Pseudo -!-
# 1. turn names_1 into Binary Search Tree
# 2. Loop through names_2
#     a. call BST.contains() methon on root 
#     b. if true
#         - push to duplicated

# -!- Data Structures -!-
# 1. Node Class
# 2. BST Class

# -!- Helper Functions -!-
# 1. BST.insert()
# 2. BST.contains()

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
        pass

# -- -- --EMD MY CODE -- -- -- #
# -- -- --EMD MY CODE -- -- -- #

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
