# Ask user for their full name
name = input("Enter full name: ").strip()

# Check if name is empty
if name == "":
    print("No name entered.")
else:
    # Split name into words
    words = name.split()

    # Check if there are 2 or 3 names
    if len(words) != 2 and len(words) != 3:
        print("Please enter 2 or 3 names.")
    else:
        # Capitalize the first and last names
        first = words[0].capitalize()
        last = words[-1].capitalize()

        # Format name and initials
        if len(words) == 2:
            print(f"Formatted: {last}, {first}")
            print(f"Initials: {first[0]}.{last[0]}.")

        else:
            # Get middle name
            middle = words[1].capitalize()

            print(f"Formatted: {last}, {first} {middle}")
            print(f"Initials: {first[0]}.{middle[0]}.{last[0]}.")
