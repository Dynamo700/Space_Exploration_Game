import random
class TreeNode:
  def __init__(self, text, choices=None):
    self.text = text
    self.choices = choices if choices else []
    self.parent = None

def story_pathes():
  #Create the story nodes and choices
  choice3a = TreeNode("You investigate the plaza") #Random encounter here
  choice3b = TreeNode("You investigate a building")
  choice3c = TreeNode("You take the left path")
  choice3d = TreeNode("You take the right path")
  choice3e = TreeNode("You go to the upper floor")
  choice3f = TreeNode("You go to the lower floor")
  choice3g = TreeNode("You investigate one of the old ships")
  choice3h = TreeNode("You investigate the storage area in the hangar")
  choice2a = TreeNode("You explore the nearby settlement", [choice3a, choice3b])
  choice2b = TreeNode("You explore the wildrness", [choice3c, choice3d])
  choice2c = TreeNode("You choose to go deeper into the space station", [choice3e, choice3f])
  choice2d = TreeNode("You decide to explore the hangar area", [choice3g, choice3h])
  choice1a = TreeNode("Explore the planet", [choice2a, choice2b])
  choice1b = TreeNode("Explore the spacestation", [choice2c, choice2d])
  root = TreeNode("You enter the Theta system. ahead of you is a planet and a spacestation", [choice1a, choice1b])

  #set the parent nodes
  choice1a.parent = root
  choice1b.parent = root
  choice2a.parent = choice1a
  choice2b.parent = choice1a
  choice2c.parent = choice1b
  choice2d.parent = choice1b
  choice3a.parent = choice2a
  choice3b.parent = choice2a
  choice3c.parent = choice2b
  choice3d.parent = choice2b
  choice3e.parent = choice2c
  choice3f.parent = choice2c
  choice3g.parent = choice2d
  choice3h.parent = choice2d

  #Add chance of finding random resource
  #Add inventory system for equipment, resources, etc. Make this through use of text file(?)

  return root

def encounter(choice):
  chance = random.randint(1,10)
  if choice.text == "You investigate the plaza" and chance == 8:
    print("You encounter a robot")
  elif choice.text == "You take the left path" and chance == 3:
    print("You encounter a beast")
  else:
    print("The coast is clear")

def random_resource(choice):
  chance = random.randint(1,25)
  if choice.text == "You investigate the storage area in the hangar" and chance == 2:
    print("You found a fuel cell would you like to pick it up?")
  else:
    print("You don't find anything")

def show_choices(choices):
  print("Choices: ")
  for i, choice in enumerate(choices):
    print(f"{i + 1}: {choice.text}")

def main():
  story_root = story_pathes()
  current_node = story_root

  print("---Welcome to the Space Exploration game!---")
  while current_node.choices:
    print(current_node.text)
    show_choices(current_node.choices)

    try:
      choice = int(input("Enter the number of your choice:  "))
      if 1 <= choice <= len(current_node.choices):
        current_node = current_node.choices[choice - 1]
        if current_node.text == "You investigate the plaza":
          encounter(current_node)
        elif current_node.text == "You take the left path":
          encounter(current_node)
        elif current_node.text == "You investigate the storage area in the hangar":
          random_resource(current_node)
      else:
        print("Attention! Invalid input. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number")

  print(current_node.text)

if __name__ == "__main__":
    main()