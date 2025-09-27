from dataStructures.Node import TreeNode


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

    def min_value(self, node=None):
        # The recursive methods uses more memory than iterative methods.

        if node is None:
            node = self.root

        if node.left is None:
            return node.value
        else:
            return self.min_value(node.left)

    def delete_node(self, value, node):
        
        if node is None:
            return None
        
        if value == self.root.value:
            self.root = None

        if value < node.value:
            node.left = self.delete_node(value, node.left)
        elif value > node.value:
            node.right = self.delete_node(value, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                sub_tree_min_val = self.min_value(node.right)
                node.value = sub_tree_min_val
                node.right = self.delete_node(node.right, sub_tree_min_val)
        return node
        
    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        
        if left > right:
            return None
        
        if (left + right) % 2 == 0:
            middle_ele = int((left + right) / 2)
        else:
            middle_ele = ((left + right) // 2) + 1

        node = TreeNode(nums[middle_ele])
        
        node.left  = self.__sorted_list_to_bst(nums, left, middle_ele - 1)
        node.right = self.__sorted_list_to_bst(nums, middle_ele + 1, right)
        
        return node
    
    def invert(self):
        self.root = self.__invert(self.root)

    def __invert(self, node):
        if node is None:
            return None
        
        temp = node.left
        node.left = node.right
        node.right = temp

        node.left = self.__invert(node.left)
        node.right = self.__invert(node.right)

        return node
    
    def tree_traversal_BFS(self):
        queue = []
        result = []
        queue.append(self.root)
        while queue:
            processing_node = queue.pop(0)
            if processing_node:
                queue.append(processing_node.left)
                queue.append(processing_node.right)
                result.append(processing_node.value)

        return result

    def tree_traversal_DFS(self):
        stack = []
        result = []
        stack.append(self.root)
        while stack:
            processing_node = stack.pop()
            if processing_node:
                stack.append(processing_node.left)
                stack.append(processing_node.right)
                result.append(processing_node.value)

        return result
    
    def tree_traversal_DFS_PreOrder_call_stack(self):
        result = []
        def traversal(node):
            if node:
                result.append(node.value)
                traversal(node.left)
                traversal(node.right)
            
        traversal(self.root)
        return result

    def tree_traversal_DFS_PostOrder_call_stack(self):
        result = []
        def traversal(node):
            if node:
                traversal(node.left)
                traversal(node.right)
                result.append(node.value)
        
        traversal(self.root)
        return result

    def tree_traversal_DFS_InOrder_call_stack(self):
        result = []
        def traversal(node):
            if node:
                traversal(node.left)
                result.append(node.value)
                traversal(node.right)
        
        traversal(self.root)
        return result

    def findMode_hashMap(self, root: TreeNode) -> list[int]:
        self.duplicates = {}

        def in_order_traversal(node):
            
            if not node:
                return

            in_order_traversal(node.left)

            if node.value not in self.duplicates:
                self.duplicates[node.value] = 1
            else:
                self.duplicates[node.value] += 1        

            in_order_traversal(node.right)

        in_order_traversal(root)

        max_dups = max(self.duplicates.values())
        ans = []
        for key, value in self.duplicates.items():

            if value == max_dups:
                ans.append(key)

        return ans

    def findMode_list(self, root: TreeNode) -> list[int]:
        
        def in_order_traversal(node, values):

            if not node:
                return
            
            in_order_traversal(node.left, values)
            values.append(node.value)
            in_order_traversal(node.right, values)

        values = []
        in_order_traversal(root, values)

        current_streak = 0
        max_streak = 0
        item = ''
        ans = []
        for val in values:

            if val != item:
                current_streak = 0

            item = val
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
                ans = []

            if current_streak == max_streak and (len(ans) == 0 or val != ans[-1]):
                ans.append(val)

        return ans

    def findMode_no_list(self, root: TreeNode) -> list[int]:
        self.prev_node = None
        self.ans = []
        self.max_streak = 0
        self.curr_streak = 0

        def in_order_traversal(node):

            if not node:
                return

            in_order_traversal(node.left)

            if self.prev_node and node.value != self.prev_node.value:
                self.curr_streak = 0

            self.curr_streak += 1
            if self.curr_streak > self.max_streak:
                self.max_streak = self.curr_streak
                self.ans = []

            if self.curr_streak == self.max_streak and (len(self.ans) == 0 or node.value != self.ans[-1]):
                self.ans.append(node.value)

            self.prev_node = node
            in_order_traversal(node.right)

        in_order_traversal(root)
        return self.ans


if __name__ == '__main__':

    '''
    my_binary_search_tree = BinarySearchTree()
    # Inserting nodes to my BST:
    print('Printing root node:', my_binary_search_tree.root)
    print('Inserting a node:', my_binary_search_tree.insert_node(47))
    print('Printing root node:', my_binary_search_tree.root.value)

    print('Inserting a node:', my_binary_search_tree.insert_node(21))
    print('Printing root\'s left node:', my_binary_search_tree.root.left.value)

    print('Inserting a node:', my_binary_search_tree.insert_node(76))
    print('Printing root\'s right node:', my_binary_search_tree.root.right.value)

    print('Inserting a node:', my_binary_search_tree.insert_node(18))
    print('Inserting a node:', my_binary_search_tree.insert_node(60))

    print('Trying inserting a duplicated node:', my_binary_search_tree.insert_node(76))

    # Checking whether a value exist within the BST:
    print('Does the tree contain the 47?:', my_binary_search_tree.contains_node(47))
    print('Does the tree contain the 21?:', my_binary_search_tree.contains_node(21))
    print('Does the tree contain the 21?:', my_binary_search_tree.contains_node(18))
    print('Does the tree contain the 76?:', my_binary_search_tree.contains_node(76))
    print('Does the tree contain the 50?:', my_binary_search_tree.contains_node(60))
    print('Does the tree contain the 21?:', my_binary_search_tree.contains_node(77))
    print('Does the tree contain the 21?:', my_binary_search_tree.contains_node(70))
    print('Does the tree contain the 21?:', my_binary_search_tree.contains_node(78))

    # Cheking the BST minimum value:
    print('BST minimum value from root:', my_binary_search_tree.min_value())
    print('BST minimum value from specified node:', my_binary_search_tree.min_value(my_binary_search_tree.root.right))

    # Deleting nodes:
    my_binary_search_tree.delete_node(18, my_binary_search_tree.root)
    print('Values after deleting 18:', my_binary_search_tree.root.left.left)

    print('BST minimum value from root:', my_binary_search_tree.min_value())
    '''

    '''
    # Convert a sorted list into a BST
    my_empty_binary_search_tree = BinarySearchTree()
    #my_empty_binary_search_tree.sorted_list_to_bst([])
    #my_empty_binary_search_tree.sorted_list_to_bst([10])
    my_empty_binary_search_tree.sorted_list_to_bst([1, 2, 3, 4, 5])
    print('Root:', my_empty_binary_search_tree.root.value)
    print('Root\'s left node:', my_empty_binary_search_tree.root.left.value)
    print('Root\'s left node:', my_empty_binary_search_tree.root.left.left.value)
    print('Root\'s left node:', my_empty_binary_search_tree.root.left.left.left)
    print('Root\'s left node:', my_empty_binary_search_tree.root.left.left.right)
    print('Root\'s left node:', my_empty_binary_search_tree.root.left.right)
    print('Root\'s right node:', my_empty_binary_search_tree.root.right.value)
    print('Root\'s right node:', my_empty_binary_search_tree.root.right.left.value)
    print('Root\'s right node:', my_empty_binary_search_tree.root.right.left.left)
    print('Root\'s right node:', my_empty_binary_search_tree.root.right.left.right)
    print('Root\'s right node:', my_empty_binary_search_tree.root.right.right)
    '''

    '''
    # Invert a BST
    my_inverted_BST = BinarySearchTree()
    my_inverted_BST.insert_node(47)
    my_inverted_BST.insert_node(21)
    my_inverted_BST.insert_node(76)
    my_inverted_BST.insert_node(18)
    my_inverted_BST.insert_node(27)
    my_inverted_BST.insert_node(52)
    my_inverted_BST.insert_node(82)

    my_inverted_BST.invert()
    print(my_inverted_BST.root.left.left.value)
    print(my_inverted_BST.root.right.right.value)
    '''

    '''
    # BFS Traversal
    my_BFS_traversal_tree = BinarySearchTree()
    my_BFS_traversal_tree.insert_node(47)
    my_BFS_traversal_tree.insert_node(21)
    my_BFS_traversal_tree.insert_node(76)
    my_BFS_traversal_tree.insert_node(18)
    my_BFS_traversal_tree.insert_node(27)
    my_BFS_traversal_tree.insert_node(52)
    my_BFS_traversal_tree.insert_node(82)
    print('\nBFS tree traversal:\n', my_BFS_traversal_tree.tree_traversal_BFS())

    # DFS Post Order Traversal
    my_DFS_traversal_tree = BinarySearchTree()
    my_DFS_traversal_tree.insert_node(47)
    my_DFS_traversal_tree.insert_node(21)
    my_DFS_traversal_tree.insert_node(76)
    my_DFS_traversal_tree.insert_node(18)
    my_DFS_traversal_tree.insert_node(27)
    my_DFS_traversal_tree.insert_node(52)
    my_DFS_traversal_tree.insert_node(82)
    print('\nDFS tree traversal:\n', my_DFS_traversal_tree.tree_traversal_DFS())
    print('\nDFS Pre Order tree traversal (call stack):\n', my_DFS_traversal_tree.tree_traversal_DFS_PreOrder_call_stack())
    print('\nDFS Post Order tree traversal (call stack):\n', my_DFS_traversal_tree.tree_traversal_DFS_PostOrder_call_stack())
    print('\nDFS In Order tree traversal (call stack):\n', my_DFS_traversal_tree.tree_traversal_DFS_InOrder_call_stack())
    '''

    # Find mode
    '''
    my_DFS_traversal_tree = BinarySearchTree()
    my_DFS_traversal_tree.insert_node(1)
    my_DFS_traversal_tree.insert_node(2)
    my_DFS_traversal_tree.root.right.left = TreeNode(2)

    #modes = my_DFS_traversal_tree.findMode_hashMap(my_DFS_traversal_tree.root)
    modes = my_DFS_traversal_tree.findMode_list(my_DFS_traversal_tree.root)
    print(modes)
    '''

    
    my_DFS_traversal_tree_hashMap = BinarySearchTree()
    my_DFS_traversal_tree_hashMap.sorted_list_to_bst([1, 7, 8, 8, 13, 20, 20])
    modes_list = my_DFS_traversal_tree_hashMap.findMode_hashMap(my_DFS_traversal_tree_hashMap.root)
    print(modes_list)
    

    
    my_DFS_traversal_tree_list = BinarySearchTree()
    my_DFS_traversal_tree_list.sorted_list_to_bst([1, 7, 8, 8, 13, 20, 20])
    modes_hash = my_DFS_traversal_tree_list.findMode_list(my_DFS_traversal_tree_list.root)
    print(modes_hash)
    


    my_DFS_traversal_tree_no_list = BinarySearchTree()
    my_DFS_traversal_tree_no_list.sorted_list_to_bst([1, 7, 8, 8, 13, 20, 20])
    modes_no_list = my_DFS_traversal_tree_no_list.findMode_no_list(my_DFS_traversal_tree_no_list.root)
    print(modes_no_list)

