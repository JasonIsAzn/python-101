# Make A Table of Items
# Resturant Menu
# Col: Appetizer, Drinks, Lunch - Meat, ALchol, Desert
# Print Order

myTableFormat = "|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|"

print(myTableFormat.format("Appetizer", "Drinks", "Main", "Alchol", "Dessert"))
print("| " + "-"*78  + "|")
print(myTableFormat.format("Mac", "Dr.Pepper", "Pizza", "Margarita", "Ice Cream"))
print(myTableFormat.format("Cheese", "Dr.Thunder", "Rib Eye", "Old Fashion", "Popcicles"))
print(myTableFormat.format("Wings", "Water", "Steak", "Cosmopolitan", "Cheesecake"))
print(myTableFormat.format("Bread", "Mt. Dew", "Baby Ribs", "Negroni", "Cake"))
print(myTableFormat.format("Corn", "Coke", "Sam Cola", "Martini", "Cookies"))
print("| " + "-"*78  + "|")

name = input("WHat's Your Name: ")
appetizer = input("Enter An Appetizer: ")
drink = input("Enter An Drink: ") 
main = input("Enter An Main: ") 
alchol = input("Enter An Alchol: ") 
dessert = input("Enter An Dessert: ") 

print("Howdy, " + name + " your order is: " )
print(appetizer, drink, main, alchol, dessert, sep=", ", end=" ")
print("Is that correct?")


ans = input("Enter (yes/no): ")
print("Thank You")



