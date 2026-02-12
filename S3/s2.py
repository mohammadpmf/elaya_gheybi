# total=0
# a = float(input("Enter price of item 1: ")) # 1.5
# total = total + a
# a = float(input("Enter price of item 2: ")) # 2
# total = total + a
# a = float(input("Enter price of item 3: ")) # 0.5
# total = total + a
# print(f"Total price is {total}")

total=0
for i in "mohammad", "elaya", "fatemeh":
    print(i)
for i in range(1, 100000000):
    aaa = float(input(f"Enter price of item {i}: "))
    total = total + aaa
    if aaa==0:
        break
print(f"Total price is {total}")


# for name in 'elaya', 'reza', 'mohammad':
#     print(name)

# for i in range(1000, 1010):
#     print(1)
#     print(2)
#     print(i)
# print(3)