import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: 
            if not self.left: 
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)
        else: 
            # if not right node
            if not self.right: 
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if value is equal to the target return true
        if self.value == target:
            # return true 
            return 1
        # if target less than the value
        if target < self.value:
            # if not left node 
            if not self.left:
                # return false 
                return 0
            else: 
                return self.left.contains(target)
        else: 
            if not self.right:
                # return false 
                return 0
            else: 
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right: 
            return self.value
        else: 
            return self.right.get_max()
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # calling cb on the value
        cb(self.value)
        # if there is left node 
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
    # Print all the values in order from low to high
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right) 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

BST = BinarySearchTree('')

for names_2 in names_2:
    BST.insert(names_2)

for names_1 in names_1:
    if BST.contains(names_1):
        duplicates.append(names_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
