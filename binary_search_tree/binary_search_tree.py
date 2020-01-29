# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare root node
        # if lesser go to left child
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else: 
                return self.left.insert(value)
        # if < or = go to right child
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)
        # if no child, on that side, insert
        # else: try again (recursion) from the child

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # look at root, if root return True
        if target == self.value:
            return True
        elif target < self.value and self.left is not None:
            return self.left.contains(target) # run recursion on self.left
        # if value < root, go left and repeat
        elif target > self.value and self.right is not None:
            return self.right.contains(target) # run recursion on self.right
        else:
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        # keep going right until theres no more
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # cb needs to touch all values
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
