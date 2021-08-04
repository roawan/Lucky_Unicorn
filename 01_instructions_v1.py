def yes_no(question):
    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "y" or response == "yes":
            response = "yes"
            return response


        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes or no")




def instructions() :
    print("***** How to Play *****")
    print()
    print("rules")
    print()
    return ""


played_before = yes_no("Have you played before?")



if played_before == "no":
    instructions()

print("Program continues")
