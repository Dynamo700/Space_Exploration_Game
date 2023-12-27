import random
def encounter(choice):
  chance = random.randint(1,10)
  if choice.text == "You investigate the plaza" and chance == 5:
    print("You encounter a robot")
  elif choice.text == "You take the left path" and chance == 3:
    print("You encounter a beast")
  else:
    print("The coast is clear")