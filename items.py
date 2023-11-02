import random
def random_resource(choice):
  chance = random.randint(1,30)
  if choice.text == "You investigate the storage area in the hangar" and chance == 2:
    print("You found a fuel cell would you like to pick it up?")
    with open("inventory.txt", "w") as file:
        file.write("fuel cell")
  elif choice.text == "You investigate the vendor tables at the edge of the plaza" and chance == 11:
    print("you find an anicent wooden necklace that looks like it's been here for years")
    with open("inventory.txt", "w") as file:
        file.write("old wooden necklace")
  elif choice.text == "Investigate study" and chance == 7:
    print("It would seem that you found a an old framed photo of a father with two children near a lake. Who knows how long it's been here..."
          "You return your ship.")
    with open("inventory.txt", "w") as file:
        file.write("old family photo")
  elif choice.text == "You investigate one of the old ships" and chance == 18:
    print("You find an fuse from the ship's engine section. These will be useful. Once you have it, you head back to your ship.")
    with open("inventory.txt", "w") as file:
        file.write("engine fuse")
  else:
        print("You don't find anything")