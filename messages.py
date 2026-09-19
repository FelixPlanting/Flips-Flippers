def welcome_message():
    print("""
Thank you for playing my little lightswitch puzzle game!
The idea is simple: you need to turn on the light in the middle by turning on all four switches at the same time.
The problem is that you don't know whether a switch is turned on or off, and after every round of flipping switches, they rotate an unknown amount of times.
To be clear, this means that they stay in the same position relative to each other, just not in the same absolute position.
You can flip switches by entering the numbers of the switches you want to flip, separated by spaces, for example like this: 1 4
Now, let's get started!
""")
    

def play_again():
    answer = input("\nWould you like to play again? y/n\n")
    if answer in ["y", "yes", "Y", "Yes"]:
        return True
    elif answer in ["n", "no", "N", "No"]:
        return False
