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
        x = self.search(key)
        if not x:
            return -1
        
        to_delete = self.root
        parent = None
        while(to_delete.key != key):
            parent = to_delete
            if(key < to_delete.key):
                to_delete = to_delete.left
            else:
                to_delete = to_delete.right

        # If leaf node
        if (to_delete.right == None and to_delete.left == None):
            if parent.left == to_delete:
                parent.left = None
            else:
                parent.right = None
            self.count -= 1
        
        # If node with one child
        if (to_delete.left == None and to_delete.right != None) or (to_delete.right == None and to_delete.left != None):
            if (to_delete.left == None):
                to_replace = to_delete.right
                to_delete.right = None
            else:
                to_replace = to_delete.left
                to_delete.left = None
            
            to_delete.key = to_replace.key
            to_delete.data = to_replace.data
            self.count -= 1
        
        # If node with two childred
        if (to_delete.right != None and to_delete.left != None):
            to_replace = to_delete.left
            to_replace_parent = None

            if to_replace.right == None:
                to_delete.key = to_replace.key
                to_delete.data = to_replace.data
                to_delete.left = None
                self.count -= 1

            else:    
                while(to_replace.right != None):
                    to_replace_parent = to_replace
                    to_replace = to_replace.right
                to_replace_parent.right = None
                to_delete.key = to_replace.key
                to_delete.data = to_replace.data            
                self.count -= 1
 
 