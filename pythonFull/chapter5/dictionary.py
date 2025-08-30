marks = {
    "Harry" : 100,
    "Shubham " : 90,
    "Ram ": 98
}
# print(marks, type(marks))
# print(marks["Harry"])

a = {
    "name " : "india",
    100 : "india",
    "marks" : [11,12,122]
}
# print(a["marks"])

# print(a.keys())

# marks.update({"mohan": 99})
# print(marks)

print(marks.get("Harry")) #Harry2 none
print(marks["Harry"])  #Harry2 error
#both are diff