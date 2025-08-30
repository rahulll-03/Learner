# Sets is the object of well defid methods 
# set is collection of non repetive method

d = {1,22,1,2,3,4,2232,223,223}
# print(d,type(d))

# e = set()

# print("empty set" ,e)
#dont use s = {} empty set they are empty dict

s = {1,2,3,2,22,3,2,3,123,"hello"}
s.add(566)

print(s)

s1 = {1,23,45,65}
s2 = {1,12,21,443,65}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.union({1,3}))
print(s2.intersection({1,4}))