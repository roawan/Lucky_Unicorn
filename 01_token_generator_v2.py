import random

tokens = ["unicorn", "donkey", "donkey", "donkey", "zebra", "horse", "horse", "horse" "zebra", "zebra"]
STARTING_BALANCE = 100


balance = STARTING_BALANCE
for i in range(0, 100):
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
