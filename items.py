import random
def random_resource(choice):
  chance = 2
  if choice.text == "You investigate the storage area in the hangar" and chance == 29:
    print("You found a fuel cell that still has some power in it. This could be useful!")
    with open("inventory.txt", "w") as file:
        file.write("fuel cell")
  elif choice.text == "You investigate the vendor tables at the edge of the plaza" and chance == 11:
    print("you find an old wooden necklace that looks like it's been here for years")
    with open("inventory.txt", "w") as file:
        file.write("old wooden necklace")
  elif choice.text == "You check in the cabinets" and chance == 7:
    print("You find an old datapad. It looks like it has been here for sometime. It has just enough power to turn on. It seems to open on a document called"
          "'Project Athena'. It seems that the document was last edited over 32 years ago.")
    with open("inventory.txt", "w") as file:
        file.write("old data pad")
  elif choice.text == "You investigate one of the old ships" and chance == 18:
    print("You find an fuse from the ship's engine section. These will be useful. Once you have it, you head back to your ship.")
    with open("inventory.txt", "w") as file:
        file.write("engine fuse")
  elif choice.text == "You check in the desk" and chance == 23:
      print("It seems you have found a key of some sort. Perhaps it unlocks a door in this building?")
      with open("inventory.txt", "w") as file:
          file.write("Mysterious key")
  elif choice.text == "You investigate the old computer terminals" and chance == 2:
      print("While poking around the computers you find that none of them can turn on, however you do find some useful components from them."
            "Some copper wires, ")
      with open("inventory.txt", "a") as file:
          file.write("copper wire\n")
      with open("inventory.txt", "a") as file:
          file.write("sticks of ram\n")
      with open("inventory.txt", "a") as file:
          file.write("motherboard\n")

  else:
        print("You don't find anything.")