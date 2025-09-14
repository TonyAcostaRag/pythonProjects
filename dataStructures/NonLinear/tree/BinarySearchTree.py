from dataStructures.Linear.Node import TreeNode


class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert_node(self, value, node=None):

        if self.root is None:
            self.root = TreeNode(value)
            return True
        
        if node is None:
            node = self.root
        
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                return True
            else:
                return self.insert_node(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
                return True
            else:
                return self.insert_node(value, node.right)
        else:
            return False

    def contains_node_iterative(self, value):
        
        pointer = self.root
        while pointer:

            if pointer.value == value:
                return True
            
            if value < pointer.value:
                pointer = pointer.left
            
            elif value > pointer.value:
                pointer = pointer.right
        
        return False
    
    def contains_node(self, value, node=None):

        if self.root is None:
            return False
        
        if node is None:
            node = self.root
        
        if value < node.value:
            if node.left is None:
                return False
            else:
                return self.contains_node(value, node.left)
        elif value > node.value:
            if node.right is None:
                return False
            else:
                return self.contains_node(value, node.right)
        else:
            return True


if __name__ == '__main__':

    my_binary_search_tree = BinarySearchTree()
    # Inserting nodes to my BST:
    print('Printing root node:', my_binary_search_tree.root)
    print('Inserting a node:', my_binary_search_tree.insert_node(47))
    print('Printing root node:', my_binary_search_tree.root.value)

    print('Inserting a node:', my_binary_search_tree.insert_node(21))
    print('Printing root\'s left node:', my_binary_search_tree.root.left.value)

    print('Inserting a node:', my_binary_search_tree.insert_node(76))
    print('Printing root\'s right node:', my_binary_search_tree.root.right.value)

    print('Trying inserting a duplicated node:', my_binary_search_tree.insert_node(76))

    # Checking whether a value exist within the BST:
    print('Does the tree contain the 47?:', my_binary_search_tree.contains_node(47))
    print('Does the tree contain the 21?:', my_binary_search_tree.contains_node(21))
    print('Does the tree contain the 76?:', my_binary_search_tree.contains_node(76))
    print('Does the tree contain the 50?:', my_binary_search_tree.contains_node(50))
