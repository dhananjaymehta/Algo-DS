# Implement a simple Binary search tree

class BST():
    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None

    def insert(self,root,val):
        #print(root.val)
        if root is None:
            root.val = val
            return

        if root.val > val:
            print(root.val,root.left,val)
            if root.left is None:
                root.left = val
                return
            else:
                self.insert(root.left, val)
        else:
        #if root.val<val:
            if root.right is None:
                root.right=val
            else:
                self.insert(root.right,val)


values=[3,4,5,6,7,8,9,1,2]
tree=BST(6)
#for i in values:
tree.insert(tree,3)
tree.insert(tree,4)
