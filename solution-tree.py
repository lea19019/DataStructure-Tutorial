"""
Some functions are own by BYU-Idaho.
This is intended only to be for teaching purposes.
"""
class BST:

    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):

        if data != node.data:
            if data < node.data:
                if node.left is None:
                    node.left = BST.Node(data)
                else:
                    self._insert(data, node.left)
            else:
                if node.right is None:
                    node.right = BST.Node(data)
                else:
                    self._insert(data, node.right)

    def __contains__(self, data):

        return self._contains(data, self.root)

    def _contains(self, data, node):

        if self.root is not None:
            if data < node.data:
                if node.left is None:
                    return False
                else:
                    return self._contains(data, node.left)
            elif data > node.data:
                if node.right is None:
                    return False
                else:
                    return self._contains(data, node.right)
            else:
                return True

    def __iter__(self):

        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
       
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):

        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):

        if node != None:
            leftHeight = self._get_height(node.left)
            rightHeight = self._get_height(node.right)
            if leftHeight > rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1
        
        return 0


def create_bst_from_sorted_list(sorted_list):

    bst = BST()
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

def _insert_middle(sorted_list, first, last, bst):

    middle = int((last + first)/2)
    
    if sorted_list:
        bst.insert(sorted_list[middle])

        sorted_list_one = sorted_list[:middle]
        _insert_middle(sorted_list_one, 0, len(sorted_list_one)-1, bst)
        
        sorted_list_two = sorted_list[middle+1:]
        _insert_middle(sorted_list_two, 0, len(sorted_list_two)-1, bst)


# ---- Solution ----

# Function to get size of tree
def get_size(BST):
    size = 0
    for x in BST:
        size = size + 1
    return size

# Create BST with given functions
tree = create_bst_from_sorted_list([5,3,7,8,1,2])
tree2 = create_bst_from_sorted_list([2,2,3,3,4,4])

# Call your function and get the size
size = get_size(tree)
size2 = get_size(tree2)

# Let's show it!
print(size)     # Returns 6
print(size2)    # Returns 3