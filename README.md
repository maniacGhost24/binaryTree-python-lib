# Binary Tree
A python library for the easy implementation of the binary tree. The library contains node structure for tree and accomplishes the following functions:

1. Insertion.
2. Deletion.
3. Traversals:
    * Inorder
    * Preorder
    * Postorder
4. Depth of tree.

## Installation Steps for local machine.
1. Clone the repo.
2. Install the following libs:
    * wheel ```pip install wheel```
    * setuptools ```pip install setuptools```
    * twine ```pip install twine```
3. Run the tests for library, from the root folder, ```python setup.py pytest```
4. If successful, build wheel, ```python setup.py bdist_wheel```
5. Using the directory from the above command finally install the library using pip ```pip install <dir>```

## Implementation tutorial

```
from binaryTree import myfunctions as bt

x = bt.Node(3) #Constructor
bt.insert(x,4) #Insertion function
bt.deletion(x,3) #Deletion function
bt.maxdepth(x) #Maxdepth
bt.inOrder(x) #Prints inorder traversal.
```