from Bst_Tree import *
from HashTable import *
import time
import random

# print("BST")
# bs_test = Bs_Tree()
# bs_test.insert(56)
# bs_test.insert(43)
# bs_test.insert(88)
# bs_test.insert(666)
# bs_test.successor(56)
# bs_test.successor(43)
# bs_test.find(666)
# bs_test.max()
#
# print("RBT")
# rbt = Rb_Tree()
# rbt.insert("blob")
# rbt.insert("klop")
# rbt.insert("ablob")
# rbt.insert("flob")
# rbt.insert("flob")
# rbt.insert("flob")
# rbt.insert("tlop")
# rbt.insert("aaalob")
# rbt.successor_node("flob")
# rbt.max()
# rbt.min()
# rbt.delete("aaalob")
# rbt.min()
# rbt.find("glob")
#
# print("HASHMAP")
# hmap = Hash(100)
# hmap.load("test.txt")
# hmap.find("therefore")
# hmap.delete("therefore")

# print("TESTING PREFERRED SIZE")
# test_results = []
#
# for x in range(100):
#     rb_test = Rb_Tree()
#     h_test = hList()
#
#     rand_arr = [random.randint(0, 1000) for _ in range(x+15)]
#
#     for element in rand_arr:
#         rb_test.insert(element)
#         h_test.insert(element)
#
#     rb_test.insert(1005)
#     h_test.insert(1005)
#
#     start1 = time.time()
#     for i in range(500000):
#         h_test.find(1005)
#         h_test.delete(1005)
#         h_test.insert(1005)
#         h_test.find(1005)
#     end1 = time.time()
#
#     start2 = time.time()
#     for i in range(500000):
#         rb_test.find(1005)
#         rb_test.delete(1005)
#         rb_test.insert(1005)
#         rb_test.find(1005)
#
#     end2 = time.time()
#     print(x+15, "LinkedList: ", end1 - start1, ", ", "RbTree: ", end2 - start2)
#     test_results.append([end1 - start1, end2 - start2])

print("TESTING LIMITS")
rb_test = Rb_Tree()
bs_test = Bs_Tree()
h_test = Hash(26)

print("     BEST CASE")

rb_test.load("dictionary.txt")
# bs_test.load("dictionary.txt")
h_test.load("dictionary.txt")

x = "A"

h_test.find(x)
print("            hmap:", h_test.bundle())

# ZA DLUGO
# bs_test.find(x)
# print("            bst:", bs_test.bundle())

rb_test.find(x)
print("            rbt:", rb_test.bundle())
