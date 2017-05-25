# Implementing a simple Binary Tree
# Insert between existing node and root.


class Tree():
    def __init__(self,nums):
        self.val=nums
        self.left=None
        self.right=None

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def insert_left(self,val):
        if self.left == None:
            self.left=Tree(val)
        else:
            tree=Tree(val)
            tree.left = self.left
            self.left = tree

    def insert_right(self,val):
        if self.right == None:
            self.right=Tree(val)
        else:
            tree=Tree(val)
            tree.left=self.right
            self.right = tree

    def inorder(self,root,res):
        if root != None:
            self.inorder(root.left,res)
            res.append(root.val)
            #print(root.val)
            self.inorder(root.right,res)
        return res

    def preorder(self,root,res):
        if root!= None:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)
        return res

    def postorder(self, root, res):
        if root != None:
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.val)
        return res

def testTree():
    myTree = Tree(1)
    myTree.insert_left(2)
    myTree.insert_right(3)
    myTree.insert_right(4)
    myTree.insert_left(5)
    myTree.insert_left(6)
    myTree.insert_right(9)
    print(myTree.inorder(myTree,[]))
    print(myTree.preorder(myTree, []))
    print(myTree.postorder(myTree, []))

# call the function
testTree()