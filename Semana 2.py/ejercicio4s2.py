print ("*** Bienvenidos a Pizza Bella Napoli *** \n")

print ("We offer a variety of ingredients for your pizza, you may choose between \n 1-Vegetarian \n 2- Non Vegetarian")

pizza_type = input ("Enter 1 for Vegetarian, enter 2 for Non Vegetarian")
if pizza_type == "1":
    print ("You chose Vegetarian pizza, here are the options \n 1- Pimientos \n 2- Tofu")
    ingredient= input ("Enter 1 for Pimientos and 2 for Tofu")
    if ingredient == "1":
        print ("Your pizza has mozzarella, tomato and Pimientos")
    elif ingredient == "2":
        print ("Your pizza has mozzarella, tomato and Tofu")

elif pizza_type == "2":
    print ("You chose Non-Vegetarian pizza, here are the options \n 1- Peperoni \n 2- Ham \n 3- Salmon")
    ingredient= input ("Enter 1 for Peperoni, enter 2 for Ham and 3 for Salmon")
    if ingredient == "1":
        print ("Your pizza has mozzarella, tomato and peperoni")
    elif ingredient == "2":
        print ("Your pizza has mozzarella, tomato and ham")
    elif ingredient == "3":
        print ("Your pizza has mozzarella, tomato and salmon")