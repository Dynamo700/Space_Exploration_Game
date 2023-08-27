class TreeNode:
  def __init__(self, text, choices=None):
    self.text = text
    self.choices = choices if choices else []
    self.parent = None

def story_pathes():
  #Create the story nodes and choices
  choice2a = TreeNode("You explore the nearby settlement")
  choice2b = TreeNode("You explore the wildrness" )
  choice2c = TreeNode("You choose to go deeper into the space station")
  choice2d = TreeNode("You decide to explore the hangar area")
  choice1a = TreeNode("Explore the planet")
  choice1b = TreeNode("Explore the spacestation")
  root = TreeNode("You enter the Theta system. ahead of you is a planet and a spacestation", [choice1a, choice1b])

  #set the parent nodes
  choice1a.parent = root
  choice1b.parent = root
  choice2a.parent = choice1a
  choice2b.parent = choice1a
  choice2c.parent = choice1b
  choice2d.parent = choice1b


  #Add random encounters

  #Add chance of finding random resource

  return root

def get_input():
  pass


def show_choices(choices):
  print("Choices: ")
  for i, choice in enumerate(choices):
    print(f"{i + 1}: {choice.text}")


def main():
  story_root = story_pathes()
  current_node = story_root

  print("---Welcome to the choose your own adventure game!---")
  while current_node.choices:
    print(current_node.text)
    show_choices(current_node.choices)

    try:
      choice = int(input("Enter the number of your choice:  "))
      if 1 <= choice <= len(current_node.choices):
        current_node = current_node.choices[choice - 1]
      else:
        print("Attention! Invalid input. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number")

  print(current_node.text)

if __name__ == "__main__":
    main()