from modules import Order2
from modules import Order3

print("Square Matrix Multiplier")
print(" ")
print("===================================")
print(" ")
a = input("Choose Order (2 or 3): ")
if a==2:
    Order2.main()
elif a==3:
    Order3.main()
else:
    print("Invalid Order! Choose either 2 or 3!")
