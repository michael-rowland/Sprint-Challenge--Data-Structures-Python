import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

'''## THIS IS O(n**2) = ~7-9 seconds'''
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

'''SOLUTION USING BINARY SEARCH TREE - O(n log n) = ~0.125 seconds'''
# bst = BSTNode(names_1[0])
# for name_1 in names_1[1:]:
#     bst.insert(name_1)
# duplicates = [i for i in names_2 if bst.contains(i)]

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

'''STRETCH SOLUTION, USING ONLY LISTS (FROM README.md) - O(n) = ~ 1.4 seconds'''
# duplicates = [i for i in names_2 if i in names_1]

'''STRETCH SOLUTION, NO RESTRICTIONS - O(1) = ~0.005 seconds
https://wiki.python.org/moin/TimeComplexity'''
names_1 = set(names_1)
duplicates = [i for i in names_2 if i in names_1]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
