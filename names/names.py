import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if value < Node's value
        if value < self.value:
            #we need to go left
            #if there is not left child,
            if self.left is None: 
                #then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            #otherwise there is a child
            else:
                #call the left child's 'insert' method
                self.left.insert(value)
        #otherwise, value >= Node's value 
        else: 
            #we need to go right
            #if we see there is not right child,
            if self.right is None:
                #then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            #otherwise there is a child 
            else:
                #call the right child's 'insert' method 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if self.value > target:
               if self.left is None:
                   return False
               return self.left.contains(target)
            else:
                if self.right is None:
                    return False
                return self.right.contains(target)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

# create a tree with all names from file 1
tree = BSTNode(names_1[0])
for elem in names_1[1:]:
    tree.insert(elem)

# search each name from file 2 in the tree
for name in names_2:
    if tree.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
