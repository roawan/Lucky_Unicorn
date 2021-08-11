import random

tokens = ["unicorn", "donkey", "zebra", "horse"]
balance = 100

for i in range(0, 20):
    chosen = random.choice(tokens)


    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    elif chosen == "horse":
        balance -= 0.5
    elif chosen == "zebra":
        balance -= 0.5


    print("Token: {} , Balance: ${}".format(chosen, balance))
