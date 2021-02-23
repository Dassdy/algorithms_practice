from graphviz import Digraph
import uuid
from random import sample

#binary tree class

class BTree(object):

    # initializition
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right
        self.dot=Digraph(comment="Binary Tree")

    # preorder traverse
    def preorder(self):
        if self.data:
            print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    # inorder traverse
    def inorder(self):
        if self.left:
            self.left.inorder()
        if self.data:
            print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    # postorder traverse
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self.data:
            print(self.data, end=' ')
        
    # levelorder traverse
    def levelorder(self):
        tree_height=self.height()
        level_order=[]
        if self.data is not None:
            level_order.append([self])
        if self.left.data or self.right.data is not None:
            for i in range(2, tree_height):
                level_nodes=[]
                for node in level_order[i-1]:
                    if node.left.data is not None:
                        level_nodes.append(node.left)
                    if node.right.data is not None:
                        level_nodes.append(node.right)
        return level_order

    # height of binary tree
    def height(self):
        if self.data is None:
            tree_height=0
        elif self.left is None and self.right is None:
            tree_height=1
        elif self.left is not None and self.right is None:
            tree_height=1+self.left.height()
        elif self.left is None and self.right is not None:
            tree_height=1+self.right.height()
        elif self.left is not None and self.right is not None:
            tree_height=1+max(self.left.height(), self.right.height())
        return tree_height

    # leaves of binary tree
    def leaves(self):

    # show the binary tree
    def print_tree(self, save_path='./Binary_Tree.gv', label=False):

        