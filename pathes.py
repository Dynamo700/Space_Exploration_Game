import random

class TreeNode:
  def __init__(self, text, choices=None):
    self.text = text
    self.choices = choices if choices else []
    self.parent = None

def story_pathes():
  #Create the story nodes and choices
  # choice6b = TreeNode
  choice6a = TreeNode("You approach a light in the distance")
  choice5a = TreeNode("Leave the plaza")
  choice5b = TreeNode("You enter the cave", [choice6a])
  choice5c = TreeNode("Investigate kitchen")
  choice5d = TreeNode("Investigate living area")
  choice5e = TreeNode("Investigate ground floor bedroom")
  choice5f = TreeNode("Investigate upstairs bedroom")
  choice5g = TreeNode("Investigate study")
  choice4a = TreeNode("You investigate the vendor tables at the edge of the plaza", [choice5a])
  choice4b = TreeNode("You go down a nearby alleyway") #death route
  choice4c = TreeNode("approach cave", [choice5b])
  choice4d = TreeNode("Approach pond") #death route
  choice4e = TreeNode("You approach the anicent monument")
  choice4f = TreeNode("You approach the statue")
  choice4g = TreeNode("You investigate the ground floor", [choice5c, choice5d, choice5e])
  choice4h = TreeNode("You investigate the upper floor", [choice5f, choice5g])
  choice3a = TreeNode("You investigate the plaza", [choice4a, choice4b]) #Random encounter here
  choice3b = TreeNode("You investigate a building", [choice4g, choice4h])
  choice3c = TreeNode("You take the left path", [choice4e, choice4f])
  choice3d = TreeNode("You take the right path", [choice4c, choice4d])
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
  choice4a.parent = choice3a
  choice4b.parent = choice3a
  choice4c.parent = choice3d
  choice4e.parent = choice3c
  choice4f.parent = choice3c
  choice4g.parent = choice3b
  choice4h.parent = choice3b
  choice4d.parent = choice3d
  choice5a.parent = choice4a
  choice5b.parent = choice4a
  choice5c.parent = choice4g
  choice5d.parent = choice4g
  choice5e.parent = choice4g
  choice5f.parent = choice4h
  choice5g.parent = choice4h
  choice6a.parent = choice5b

  #Add chance of finding random resource
  #Add inventory system for equipment, resources, etc. Make this through use of text file(?)

  return root

def game_events(choice):
  if choice.text == "You take the left path":
    print("Before you is an anicent monument and a statue of a dragon. Which would you like to investigate?")
  elif choice.text == "You approach the anicent monument":
    print("As you approach the monument you see that there is alien writing on sections of the monument")
    print("Suddenley the writing begins to glow blue, and energy forms around you, as you are teleported away from the planet...")
  elif choice.text == "You approach the statue":
    print("The statue was nearly 10 feet tall and seems to be humanoid shaped but has a wolf's head, hands and feet")
    print("You hear faint...Whispering as you approach.")
    print("Suddenley the statue moves toward you, it's eyes glowing blue, it presentes you with a mysterious sword.")
def found_item(choice):
  pass
def end_game_events(choice):
  if choice.text == "You go down a nearby alleyway":
    print("You fall down a sewer grate and die.")
  elif choice.text == "Approach pond":
    print("Suddenley a large reptilian creature comes up from the water and eats you!")
  elif choice.text == "You approach a light in the distance":
    print("You find a teal crystal that appears to have specks of blue within it. This is what was giving off that signal")
    with open("inventory.txt", "w") as file:
        file.write("mysterious alien crystal")
def encounter(choice):
  chance = random.randint(1,10)
  if choice.text == "You investigate the plaza" and chance == 8:
    print("You encounter a robot")
  elif choice.text == "You take the left path" and chance == 3:
    print("You encounter a beast")
  else:
    print("The coast is clear")

def random_resource(choice):
  chance = 2
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
          game_events(current_node)
        elif current_node.text == "You investigate the storage area in the hangar":
          random_resource(current_node)
        elif current_node.text == "You investigate the vendor tables at the edge of the plaza":
          random_resource(current_node)
        elif current_node.text == "You go down a nearby alleyway":
          end_game_events(current_node)
        elif current_node.text == "Approach pond":
          end_game_events(current_node)
        elif current_node.text == "You approach a light in the distance":
          end_game_events(current_node)
        elif current_node.text == "You approach the anicent monument":
          game_events(current_node)
        elif current_node.text == "You approach the statue":
          game_events(current_node)
      else:
        print("Attention! Invalid input. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number")

  print(current_node.text)

if __name__ == "__main__":
    main()