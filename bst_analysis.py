





# IMPORT REQUIRED LIBRARIES




import random
import matplotlib.pyplot as plt
import os




# CLASS TO REPRESENT A NODE IN THE TREE




class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None




        self.height = 1  # USED FOR AVL TREE





# CLASS FOR A REGULAR BINARY SEARCH TREE




class BST:
    def __init__(self):
        self.root = None





    # INSERT A NEW VALUE INTO THE TREE






    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root



    # CALCULATE THE HEIGHT OF THE TREE


    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))


    # CALCULATE THE IMBALANCE BETWEEN LEFT AND RIGHT SUBTREES


    def get_imbalance(self, node):
        if not node:
            return 0
        return abs(self.get_height(node.left) - self.get_height(node.right))



# CLASS FOR AVL TREE THAT INHERITS FROM BST


class AVL(BST):


    # LEFT ROTATION FUNCTION


    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y



    # RIGHT ROTATION FUNCTION


    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y



    # CALCULATE BALANCE FACTOR


    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    




    # INSERT VALUE WITH AVL BALANCING



    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)



        balance = self.get_balance(root)





        # LEFT LEFT CASE



        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        


        # RIGHT RIGHT CASE



        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        


        # LEFT RIGHT CASE



        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        


        # RIGHT LEFT CASE



        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        

    

        return root



# LISTS TO STORE HEIGHTS AND IMBALANCES FOR 1000 TREES


bst_heights = []
bst_imbalances = []




N = 1000  # NUMBER OF RANDOM TREES TO GENERATE



for _ in range(N):




    # CREATE A RANDOM SEQUENCE OF NUMBERS FROM 1 TO 20




    sequence = random.sample(range(1, 21), 20)
    bst = BST()
    root = None
    for num in sequence:
        root = bst.insert(root, num)
    bst_heights.append(bst.get_height(root))
    bst_imbalances.append(bst.get_imbalance(root))





# CREATE HISTOGRAM FOR TREE HEIGHTS




plt.hist(bst_heights, bins=range(min(bst_heights), max(bst_heights)+1), edgecolor='black')
plt.title("Histogram of BST Heights")
plt.xlabel("Height")
plt.ylabel("Frequency")
os.makedirs("BST_Project", exist_ok=True)

plt.savefig("BST_Project/bst_height_histogram.png")
plt.clf()



# CREATE HISTOGRAM FOR TREE IMBALANCES




plt.hist(bst_imbalances, bins=range(min(bst_imbalances), max(bst_imbalances)+1), edgecolor='black')
plt.title("Histogram of BST Imbalance")
plt.xlabel("Imbalance")
plt.ylabel("Frequency")
plt.savefig("BST_Project/bst_imbalance_histogram.png")
