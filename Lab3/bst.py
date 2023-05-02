class BinarySearchTree:
    def __init__(self):
        self.count = 0
        self.root = None
    
    class Node:
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.left = None
            self.right = None
    
    
    def size(self):
        return self.count
    

    def add(self, key, value):        
        z = self.Node(key, value)
        y = None
        x = self.root
        while(x != None):
            y = x
            if(key <  x.key):
                x = x.left
            else:
                x = x.right
        
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
            
        self.count += 1
    
    def inorder_walk(self):
        values = []
        self._inorder_walk(self.root, values)
        return values
    
    def _inorder_walk(self, node, values):
        if node is not None:
            self._inorder_walk(node.left, values)
            values.append(node.key)
            self._inorder_walk(node.right, values)
    
    def postorder_walk(self):
        values = []
        self._postorder_walk(self.root, values)
        return values

    def _postorder_walk(self, node, values):
        if node is not None:
            self._postorder_walk(node.left, values)
            self._postorder_walk(node.right, values)
            values.append(node.key)
        
    def preorder_walk(self):
        values = []
        self._preorder_walk(self.root, values)
        return values

    def _preorder_walk(self, node, values):
        if node is not None:
            values.append(node.key)
            self._preorder_walk(node.left, values)
            self._preorder_walk(node.right, values)

    def smallest(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return (node.key, node.value)
    

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if node is None:
            return False
        elif node.key == key:
            return node.data
        elif key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)
        
    def smallest(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return (node.key, node.data)
    

    def largest(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return (node.key, node.data)

    def remove(self, key):
        if not self.root:
            return

        current_node = self.root
        parent_node = None

        # Find the node to be removed and its parent.
        while current_node and current_node.key != key:
            parent_node = current_node

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # If the node was not found, return.
        if not current_node:
            return

        # If Node has no children
        if not current_node.left and not current_node.right:
            if current_node == self.root:
                self.root = None
            elif current_node.key < parent_node.key:
                parent_node.left = None
            else:
                parent_node.right = None

        # If Node has one child
        elif (current_node.left and not current_node.right) or (not current_node.left and current_node.right):
            if current_node.left:
                child_node = current_node.left
            else:
                child_node = current_node.right

            if current_node == self.root:
                self.root = child_node
            elif current_node.key < parent_node.key:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        # If Node has two children
        else:
            successor_parent_node = current_node
            successor_node = current_node.right
            while successor_node.left:
                successor_parent_node = successor_node
                successor_node = successor_node.left

            current_node.key = successor_node.key
            current_node.data = successor_node.data

            if successor_parent_node == current_node:
                successor_parent_node.right = successor_node.right
            else:
                successor_parent_node.left = successor_node.right

        self.count -= 1

 
 