# Ask user to enter a password
password = input("Enter password: ")

# Check if password is empty
if password == "":
    print("No password entered.")
else:
    # Check password requirements
    length = len(password) >= 8
    upper = password != password.lower()
    lower = password != password.upper()
    symbol = "!" in password or "@" in password or "#" in password or "$" in password

    # Print results for each check
    print("Length (8+):", "PASS" if length else "FAIL")
    print("Uppercase:", "PASS" if upper else "FAIL")
    print("Lowercase:", "PASS" if lower else "FAIL")
    print("Symbol (!@#$):", "PASS" if symbol else "FAIL")

    # Add up passed checks
    score = length + upper + lower + symbol

    # Decide password strength
    if score <= 1:
        rating = "Weak"
    elif score <= 3:
        rating = "Medium"
    else:
        rating = "Strong"

    # Display final score and rating
    print(f"Score: {score}/4 - {rating}")
