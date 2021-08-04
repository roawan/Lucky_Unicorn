# function
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"
# main routine





    valid = False
    while not valid:
        try:
           # ask question
            response = int(input(question))
            # if amount is too low / too high give
            if low < response <= high:
               return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

how_much = num_check("how much would you like to play with?", 0, 10)
