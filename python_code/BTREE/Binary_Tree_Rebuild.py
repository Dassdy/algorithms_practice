# -*- coding: utf-8 -*-  
from Binary_Tree import BTree

def BTree_Rebuild(treeArray):

    binaryTree=[]
    if treeArray is None:
        binaryTree=None
    elif len(treeArray) == 1:
        binaryTree.append(BTree(treeArray[0]))
        binaryTree[0].left=None
        binaryTree[0].right=None
    else:
        lastParentNodeIndex=int(len(treeArray)/2)
        for i in range(0, len(treeArray)):
            binaryTree.append(BTree(data=treeArray[i]))
        for i in range(1, lastParentNodeIndex+1):
            binaryTree[i-1].left=binaryTree[2*i-1]
            if 2*i+1<=len(treeArray):
                binaryTree[i-1].right=binaryTree[2*i]
    return binaryTree[0]

arrayOfTree='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rebuiltedTree=BTree_Rebuild(arrayOfTree)
print('先序遍历为:')
rebuiltedTree.preorder()
print()

print('层序遍历为:')
level_order = rebuiltedTree.levelorder()
print(level_order)
print()

height = rebuiltedTree.height()
print('树的高度为%s.' % height)

print('叶子节点为：')
rebuiltedTree.leaves()
print()

rebuiltedTree.print_tree(label=True)