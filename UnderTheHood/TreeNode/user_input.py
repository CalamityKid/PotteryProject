def input_cast():
    """aux method, takes an input and tries to cast it to int, 
    if it succeeds returns the int, 
    if it fails 3 times returns None"""
    strikes = 3
    while True: 
        user_input = input ("\nSelect a number: ")
        try:
            user_input_int = int(user_input)
            return user_input_int

        except (ValueError, TypeError):
            print (f"\n{user_input} not valid. Please type one of the numbers above.\n")
            strikes -=1
            if strikes == 0:
                return None

def yes_or_no ():
    "Takes a yes or no input, returns bool"
    while True:
        user_input = input ("Yes or no? ")
        user_input = user_input.lower()
        if user_input == ("yes" or "y"):
            return True
        elif user_input == ("no" or "n"):
            return False
        print ("Not a valid option. \n")

        

def select_categories (superclass_cat):
    """Given a superclass, selects a subclass from an input, 
    returns the subclass"""
    while True:
        while True:
            print("")
            for key, value in superclass_cat.str_categories.items():
                print (f"Write {key} for {value}")
        
            user_input_int = input_cast()
            if user_input_int != None:
                break
        
        if user_input_int in superclass_cat.class_categories:

            return superclass_cat.class_categories[user_input_int]
        else: 
            print ("\nThat number is our of range.\n")