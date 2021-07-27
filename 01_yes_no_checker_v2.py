# ask user if they've played before
show_instructions = input("Have you played before").strip().lower()
# if they say yes, continue program
if show_instructions == "y" or show_instructions == "yes":
    print("program continues")

# if no, display instructions then continue
elif show_instructions == "no" or show_instructions == "n":
    print("show instructions")

# unexpected response
else:
    print("Please answer yes or no")
