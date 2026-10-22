# --- Age Eligibility Check ---
age = float(input("Enter your age: "))
print(f"Your age is: {age}")

if age < 18 and age >= 15:
    print("You will require parental consent to participate.")
elif age >= 18:
    print("You are eligible to participate without parental consent.")
else:
    print("Not eligible to participate.")

# --- For Loop Example ---
print("\nCounting by 2s up to 10:")
for x in range(0, 11, 2):
    print(x)

# --- While Loop: Password Security ---
authenticated = False
while not authenticated:
    password = input("Enter your password: ")
    if password == "Python":
        print("Access Granted!")
        authenticated = True
    else:
        print("Wrong password. Please try again.")
