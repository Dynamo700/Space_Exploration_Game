def end_game_events(choice):
  if choice.text == "You go down a nearby alleyway":
    print("You fall down a sewer grate and die.")
  elif choice.text == "Approach pond":
    print("Suddenley a large reptilian creature comes up from the water and eats you!")
  elif choice.text == "You approach a light in the distance":
    print("You find a teal crystal that appears to have specks of blue within it. This is what was giving off that signal")
    with open("inventory.txt", "w") as file:
        file.write("mysterious alien crystal")