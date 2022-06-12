import random

while True:
    
    user = input("Pick an option R, P OR S: ").capitalize()
    options = ["R", "P", "S"]
    computer = random.choice(options)

    if user == computer:
        print("It's a tie!")
    elif user == "R":
        if computer == "S":
            print(f"Player (Rock): CPU (Scissors)\n Winner: User")
        else:
            print(f"Player (Scissors): CPU (Rock)\n Winner: Computer")
    elif user == "P":
        if computer == "R":
            print(f"Player (Paper): CPU (Rock)\n Winner: User")
        else:
            print(f"Player (Rock): CPU (Paper)\n Winner: Computer")
    elif user == "S":
        if computer == "P":
            print(f"Player (Scissors): CPU (Paper)\n Winner: User")
        else:
            print(f"Player (Paper): CPU (Scissors)\n Winner: Computer")
    else:
        print("Error, please enter a valid option")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break