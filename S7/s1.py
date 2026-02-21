try:
    age = int(input("Enter your age: "))
    print(f"You will be {age+1} years old nex year.")
except ModuleNotFoundError:
    print("Enter a number. It is not a number.")
except ZeroDivisionError:
    print('333')
except ValueError:
    print(333444)
except:
    print("Unknown error")
print("continue the program")
