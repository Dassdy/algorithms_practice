from __future__ import print_function
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
        if self.left or self.right is not None:
            for i in range(2, tree_height+1):
                level_nodes=[]
                for node in level_order[i-2]:
                    if node.left is not None:
                        level_nodes.append(node.left)
                    if node.right is not None:
                        level_nodes.append(node.right)
                level_order.append(level_nodes)

        for i in range(len(level_order)):
            for index in range(len(level_order[i])):
                level_order[i][index] = level_order[i][index].data
 
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
        if self.data is None:
            return None
        if self.left is None and self.right is None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.leaves()
        if self.right is not None:
            self.right.leaves()

    # show the binary tree
    def print_tree(self, save_path='./Binary_Tree.jpg', label=False):
        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']
        # draw one binary tree of one node as root node
        def print_node(node, node_tag):
            # node's color
            color = sample(colors,1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())
                # data of node
                self.dot.node(left_tag, str(node.left.data), style='filled', color=color)
                label_string = 'L' if label else ''    
                # whether tag on the line to show left sub-tree
                self.dot.edge(node_tag, left_tag, label=label_string)   
                # line of left node and parent node
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, str(node.right.data), style='filled', color=color)
                label_string = 'R' if label else '' 
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        if self.data is not None:
            root_tag = str(uuid.uuid1())                
            # root node label
            self.dot.node(root_tag, str(self.data), style='filled', color=sample(colors,1)[0])
            print_node(self, root_tag)

        self.dot.render(save_path)                            