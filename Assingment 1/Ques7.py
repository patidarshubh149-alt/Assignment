# Program to calculate the simple intrest.
# (Formula: SI = (P * R * T)/100)

P = int(input("The initial amount of money borrowed: "))
R = int(input("Rate of Interest: "))
T = int(input("Time Duration: "))

SI = (P * R * T)/100
print("Total intrest Earned: ",SI)
