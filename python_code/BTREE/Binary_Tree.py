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

    # height of binary tree
    def height(self):

    # leaves of binary tree
    def leaves(self):

    # show the binary tree
    def print_tree(self, save_path='./Binary_Tree.gv', label=False):

        