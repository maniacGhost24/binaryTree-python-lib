#Node for the binary tree.
class Node:
    def __init__(self,key: int):
        self.left = None
        self.right = None
        self.data = key

#Inorder Traversal for the Tree.
def inOrder(temp:Node):

    if not temp:
        return
    
    inOrder(temp.left)
    print(temp.data,end = " ")
    inOrder(temp.right)

#Delete Deepest Node in the tree.
def deleteDeepest(root:Node,d_node:Node):
    q = []
    q.append(root)

    while(len(q)):
        temp = q.pop(0)

        if temp is d_node:
            temp = None
            return
        
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

#delete element in binary tree.
def deletion(root:Node,key:int):
    if not root:
        return None
    
    if ((not root.left) and (not root.right)):
        if root.key == key:
            return None
        else:
            return root

    key_node = None
    q = []
    q.append(root)

    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node:
        x = temp.data
        deleteDeepest(root,temp)
        key_node.data = x
    return root 

#Level order insertion function for tree.
def insert(root:Node,key:int):

    if not root:
        root = Node(key)
        return root
    
    q = []
    q.append(root)

    while(len(q)):
        root = q[0]
        q.pop(0)

        if not root.left:
            root.left = Node(key)
            break
        else:
            q.append(root.left)
        
        if not root.right:
            root.right = Node(key)
            break
        else:
            q.append(root.right)