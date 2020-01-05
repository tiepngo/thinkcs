"""
    This is example to show 3 differ assign "="
"""

# Case 1 : Normal assign
origin_case1 = [1,2,3,[4,5]]
clone1 = origin_case1
print("Case_1 origin value : {}".format(origin_case1))
clone1[2] = 99
clone1.append(99)
print("Case_1 origin value after change clone : {}".format(origin_case1))
print("Clone value                            : {}".format(clone1))
print("End case 1")

# Case 2 : Shallow copy method
import copy
origin_case2 = [1,2,3,[4,5]]
clone2 = copy.copy(origin_case2)
print("Case_2 origin value : {}".format(origin_case2))
clone2[2] = 99
clone2[3].append(99)
clone2.append(99)
print("Case_2 origin value after change clone : {}".format(origin_case2))
print("Clone value                            : {}".format(clone2))

# Case 3 : Deep copy
origin_case3 = [1,2,3,[4,5]]
clone3 = copy.deepcopy(origin_case3)
print("Case_3 origin value : {}".format(origin_case3))
clone3[2] = 99
clone3[3].append(99)
clone3.append(99)
print("Case_3 origin value after change clone : {}".format(origin_case3))
print("Clone value                            : {}".format(clone3))