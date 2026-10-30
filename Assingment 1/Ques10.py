#Program that asks the user for a number and prints the multiplication table of that number up to 10.

num = int(input("Enter the number: "))

for i in range(1,11):
    total = num*i
    print(f"{num} * {i} = ",total)
print()