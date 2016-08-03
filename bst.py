import queue
class Tree:
    """
    Represents a binary search tree
    """
    def __init__(self):
        """
        Tree constructor.
        """
        self.root = None

    def insert(self, key):
        """
        Insert a node into tree
        :param key: value of the element to be inserted
        :return: void
        """
        if (self.root == None):
            self.root = TreeNode(key)
        else:
            self.root.insert(key)

    
    def preOrderTraversal(self):
        """
        Pre Order Traversal of the Tree. i.e. root -> left -> right
        :return:
        """
        self.root.preOrder()

    def inOrderTraversal(self):
        """
        In Order traversal of the tree. i.e. left -> root -> right
        this prints the data in sorted order
        :return:
        """
        self.root.inOrder()
    def postOrderTraversal(self):
        """
        Post Order traversal of the tree. i.e. left -> right -> root
        :return:
        """
        self.root.postOrder()

    def levelOrderTraversal(self):
        self.root.levelOrder()
        
    def remove(self, key):
        """
        remove the node that contains the key
        :param key:
        :return:
        """
        if self.root:
            self.root.remove(key)

class TreeNode:
    """
    Represents a node in the tree
    """
    def __init__(self, key):
        """
        TreeNode Constructor
        :param key:
        """
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        """
        insert a node
        """

        # if the key we're trying to insert is smaller than the current node's key and there is a left sub tree
        # then insert the key in the left sub-tree
        # else create a node with the key as the left child
        if self.key > key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = TreeNode(key)

        # if the key we're trying to insert is greater than the current node's key and there is a right sub tree
        # then insert the key in the right sub tree
        # else create a node with the key as the right child
        elif self.key < key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = TreeNode(key)


    def remove(self, key):
        """
        remove the node that contains the key
        """

        # we will keep track of the parent to help us update references
        node, parent = self, None

        # keep going till we've found the node we're looking for or we've concluded that the given key is not present
        # in the tree
        while node is not None and key != node.key:
            parent = node
            # if they current key is greater search in the left sub-tree else search in the right sub tree
            if node.key > key:
                node = node.left
            else:
                node = node.right

        # if node is None, it means that we didn't find the key to delete and we return
        if node is None:
            return

        # if there are no child to the node containing data and it a left child of it's parent then set the left child
        # of the parent to None. Else set the right child of the parent to None.
        # Essentially removing the node from the parent
        if node.left is None and node.right is None:
            if parent.key > node.key:
                parent.left = None
            else:
                parent.right = None
        # if left child is None, meaning the node we're trying to delete has a right child
        # replace the node containing the data with it's right sub tree by updating the parent's child reference
        elif node.left is None:
            if parent.key > node.key:
                parent.left = node.right
            else:
                parent.right = node.right
        # if right child is None, meaning the node we're trying to delete has a left child
        # replace the node containing the data with it's left  sub tree by updating the parent's child reference
        elif node.right is None:
            if parent.key > node.key:
                parent.left = node.left
            else:
                parent.right = node.left
        # when the node we're trying to remove has both a left and a right child. replace it with the min from the
        # right sub tree and then removing the min node from the right sub tree.
        # alternatively, we could have replaced the node with max from the left sub tree and delete the max node in
        # the left sub tree
        else:
            node.key = self.findMin(node.right)
            node.right.remove(node.key)

    def findMin(self, node):
        """
        helper functiont to find min. Smallest node in a BST or a subtree of a BST has to be the left most node
        so, we find the left most node and return it's key value
        :param node:
        :return:
        """
        while node.left:
            node = node.left
        return node.key

    def preOrder(self):
        """
        pre order traversal
        :return:
        """
        if self:
            print(self.key)
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()

    def inOrder(self):
        """
        in order traversal
        :return:
        """
        if self:
            if self.left:
                self.left.inOrder()
            print(self.key)
            if self.right:
                self.right.inOrder()

    def postOrder(self):
        """
        post order traversal
        :return:
        """
        if(self):
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print(self.key)

    def levelOrder(self):
        if(self):
            que = queue.Queue()
            que.enqueue(self)
            while que.front != que.back:
                node = que.peek()
                print(node.key)
                que.dequeue()
                if node.left:
                    que.enqueue(node.left)
                if node.right:
                    que.enqueue(node.right)

def test():
    """
    test function
    :return:
    """
    tree = Tree()
    tree.insert(40)
    tree.insert(30)
    tree.insert(35)
    tree.insert(20)
    tree.insert(25)
    tree.insert(50)
    tree.insert(55)
    tree.insert(45)
    tree.insert(47)
    tree.inOrderTraversal()
    print()
    tree.inOrderTraversal()
    print()
    tree.preOrderTraversal()
    print()
    tree.postOrderTraversal()
    print()
    tree.levelOrderTraversal()

if __name__ == '__main__':
    test()
