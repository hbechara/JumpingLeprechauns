# Define a class for nodes
class Node:
    def __init__(self, key):
        self.key = key # The value stored in the node
        self.left = None # The left child of the node
        self.right = None # The right child of the node
        self.height = 1 # The height of the node
        self.parent = None # The parent of the node

# Define a class for AVL tree
class AVLTree:
    def __init__(self):
        self.root = None # The root of the tree

    # A utility function to get the height of a node
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # A utility function to get the balance factor of a node
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # A utility function to perform right rotation
    def right_rotate(self, z):
        y = z.left # Store the left child of z
        T3 = y.right # Store the right subtree of y

        # Perform rotation
        y.right = z # Make z as the right child of y
        z.left = T3 # Make T3 as the left child of z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Update parents
        y.parent = z.parent # Make y as the child of z's parent
        if y.parent is None: # If y's parent is None, make y as the root
            self.root = y
        elif y.parent.left == z: # If z was the left child of its parent, make y as the left child
            y.parent.left = y
        else: # If z was the right child of its parent, make y as the right child
            y.parent.right = y
        z.parent = y # Make y as the parent of z
        if T3 is not None: # If T3 is not None, make z as its parent
            T3.parent = z

        # Return the new root
        return y

    # A utility function to perform left rotation
    def left_rotate(self, z):
        y = z.right # Store the right child of z
        T2 = y.left # Store the left subtree of y

        # Perform rotation
        y.left = z # Make z as the left child of y
        z.right = T2 # Make T2 as the right child of z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Update parents
        y.parent = z.parent # Make y as the child of z's parent
        if y.parent is None: # If y's parent is None, make y as the root
            self.root = y
        elif y.parent.left == z: # If z was the left child of its parent, make y as the left child
            y.parent.left = y
        else: # If z was the right child of its parent, make y as the right child
            y.parent.right = y
        z.parent = y # Make y as the parent of z
        if T2 is not None: # If T2 is not None, make z as its parent
            T2.parent = z

        # Return the new root
        return y



    # A utility function to insert a node in the AVL tree
    def insert(self, key):
        # Perform standard BST insert
        node = Node(key) # Create a new node with the given key
        if self.root is None: # If the tree is empty, make the new node as the root
            self.root = node
            return
        current = self.root # Start from the root
        while current is not None: # Traverse the tree until a leaf is reached
            if key < current.key: # If the key is smaller than the current node's key, go to the left subtree
                if current.left is None: # If the left child is None, insert the new node there
                    current.left = node
                    node.parent = current # Make current as the parent of node
                    break
                else: # If the left child is not None, go to the next level
                    current = current.left
            else: # If the key is larger than or equal to the current node's key, go to the right subtree
                if current.right is None: # If the right child is None, insert the new node there
                    current.right = node
                    node.parent = current # Make current as the parent of node
                    break
                else: # If the right child is not None, go to the next level
                    current = current.right

        # Update heights and balance factors of all ancestors of node
        while node is not None:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)) # Update height of node
            balance = self.get_balance(node) # Get balance factor of node

            # If node is unbalanced, perform rotations to balance it
            if balance > 1: # Left subtree is heavier than right subtree
                if key < node.left.key: # Left Left case
                    node = self.right_rotate(node) # Perform right rotation on node
                else: # Left Right case
                    node.left = self.left_rotate(node.left) # Perform left rotation on left child of node
                    node = self.right_rotate(node) # Perform right rotation on node
            elif balance < -1: # Right subtree is heavier than left subtree
                if key > node.right.key: # Right Right case
                    node = self.left_rotate(node) # Perform left rotation on node
                else: # Right Left case
                    node.right = self.right_rotate(node.right) # Perform right rotation on right child of node
                    node = self.left_rotate(node) # Perform left rotation on node

            # Move to the parent of node and repeat until root is reached
            node = node.parent