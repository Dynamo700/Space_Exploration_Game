from events import game_events
from ends import end_game_events
from encounters import encounter
from items import random_resource
class TreeNode:
  def __init__(self, text, choices=None):
    self.text = text
    self.choices = choices if choices else []
    self.parent = None

def story_pathes():
  #Create the story nodes and choices
  choice6g = TreeNode("You check in the cabinets")
  choice6f = TreeNode("You check in the desk")
  choice6e = TreeNode("It seems that nothing is here. Time to head back to your ship.")
  choice6d = TreeNode("It seems that nothing is here. Time to head back to your ship.")
  choice6c = TreeNode("You don't find anything. You decide to head back to your ship.")
  choice6b = TreeNode("You investigate the kitchen and you don't find anything. You decide to head back to your ship.")
  choice6a = TreeNode("You approach a light in the distance")
  choice5a = TreeNode("Leave the plaza")
  choice5b = TreeNode("You enter the cave", [choice6a])
  choice5c = TreeNode("Investigate kitchen", [choice6b])
  choice5d = TreeNode("Investigate living area", [choice6c])
  choice5e = TreeNode("You investigate the closet", [choice6e])
  choice5f = TreeNode("Investigate upstairs bedroom", [choice6d])
  choice5g = TreeNode("Investigate study", [choice6f, choice6g])
  choice5h = TreeNode("You investigate the old computer terminals")
  choice5i = TreeNode("You investigate the control room")
  choice4a = TreeNode("You investigate the vendor tables at the edge of the plaza", [choice5a])
  choice4b = TreeNode("You go down a nearby alleyway") #death route
  choice4c = TreeNode("approach cave", [choice5b])
  choice4d = TreeNode("Approach pond") #death route
  choice4e = TreeNode("You approach the anicent monument")
  choice4f = TreeNode("You approach the statue")
  choice4g = TreeNode("You investigate the ground floor", [choice5c, choice5d, choice5e])
  choice4h = TreeNode("You investigate the upper floor", [choice5f, choice5g])
  choice4i = TreeNode("You head to the control room", [choice5h, choice5i])
  choice3a = TreeNode("You investigate the plaza", [choice4a, choice4b]) #Random encounter here
  choice3b = TreeNode("You investigate a building", [choice4g, choice4h])
  choice3c = TreeNode("You take the left path", [choice4e, choice4f])
  choice3d = TreeNode("You take the right path", [choice4c, choice4d])
  choice3e = TreeNode("You go to the upper floor", [choice4i])
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
  choice4i.parent = choice3e
  choice5a.parent = choice4a
  choice5b.parent = choice4a
  choice5c.parent = choice4g
  choice5d.parent = choice4g
  choice5f.parent = choice4h
  choice5g.parent = choice4h
  choice5h.parent = choice4i
  choice5i.parent = choice4i
  choice6a.parent = choice5b
  choice6b.parent = choice5c
  choice6c.parent = choice5d
  choice6d.parent = choice5f
  choice6e.parent = choice5e
  choice6f.parent = choice5g
  choice6g.parent = choice5g



  #Add chance of finding random resource
  #Add inventory system for equipment, resources, etc. Make this through use of text file(?)

  return root

#Move these to different modules
choice = TreeNode("You approach the anicent monument")
game_events(choice)

choice = TreeNode("You go down a nearby alleyway")
end_game_events(choice)

choice = TreeNode("You investigate the plaza")
encounter(choice)

choice = TreeNode("You investigate the storage area in the hangar")
random_resource(choice)

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
        elif current_node.text == "You check in the desk":
          random_resource(current_node)
        elif current_node.text == "You check in the cabinets":
          random_resource(current_node)
        elif current_node.text == "You investigate one of the old ships":
          random_resource(current_node)
        elif current_node.text == "You investigate the old computer terminals":
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