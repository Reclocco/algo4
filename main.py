import sys
from Bst_Tree import Bs_Tree
from Rb_Tree import Rb_Tree
from HashTable import Hash

structure = None

if sys.argv[1] == "--type":
    if sys.argv[2] == "bst":
        structure = Bs_Tree()
    elif sys.argv[2] == "rbt":
        structure = Rb_Tree()
    elif sys.argv[2] == "hamp":
        structure = Hash(26)

lines = int(input())
for _ in range(lines):
    choice = input().split()
    if choice[0] == "insert":
        structure.insert(choice[1])
    elif choice[0] == "delete":
        structure.delete(choice[1])
    elif choice[0] == "find":
        structure.find(choice[1])
    elif choice[0] == "load":
        structure.load(choice[1])
    elif choice[0] == "min":
        structure.min()
    elif choice[0] == "max":
        structure.max()
    elif choice[0] == "succesor":
        structure.successor(choice[1])
    elif choice[0] == "inorder":
        structure.inorder()
