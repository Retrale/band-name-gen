#band name generator project one.

#welcome message
print("Welcome to the random name generator.")

start = True

while True:
    #Take 2 variables as user input, city grew up in and name of your pet.
    city = input("What is the name of the city you grew up in? ")
    pet = input("What is the breed of your pet? ")

    #Add variables together and print

    band_name = ("Your band name could be: The " + city + " " + pet + "s")
    print(band_name)
    again = input("Would you like to try again? y/n")
    if again == "n":
        break

