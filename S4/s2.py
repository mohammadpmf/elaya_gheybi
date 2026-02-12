total=0
i=1
aaa = float(input(f"Enter price of item {i}: "))
while aaa!=0:
    total = total + aaa
    # i = i+1
    i += 1
    aaa = float(input(f"Enter price of item {i}: "))

print(f"Total price is {total}")

# 1
# 3
# 5
# 7
# 9
# .
# 73
