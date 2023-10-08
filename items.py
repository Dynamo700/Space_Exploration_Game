import random
def random_resource(choice):
  chance = random.randint(1,25)
  if choice.text == "You investigate the storage area in the hangar" and chance == 2:
    print("You found a fuel cell would you like to pick it up?")
    with open("inventory.txt", "w") as file:
        file.write("fuel cell")
  elif choice.text == "You investigate the vendor tables at the edge of the plaza" and chance == 11:
    print("you find an anicent wooden necklace that looks like it's been here for years")
    with open("inventory.txt", "w") as file:
        file.write("old wooden necklace")
  else:
    print("You don't find anything")