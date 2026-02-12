#                  0          1         2         3       4
names_tuple = ("Mohammad", "Elaya", "Fatemeh", "Elaya", "Sara")
print(names_tuple, type(names_tuple))
print(names_tuple.count("Elaya"))
print(names_tuple.index("Sara"))


names_list = ["Mohammad", "Elaya", "Fatemeh", "Elaya", "Sara"]
names_list.sort()
names_list.append("Hela")
names_list.insert(2, "Ali")
print(names_list)
names_list.reverse()
print(names_list)

empty_list = []