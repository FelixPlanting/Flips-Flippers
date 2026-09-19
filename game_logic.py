import random
import flip_switches

def game():
    switches = [1, 1, 1, 1]
    while switches == [1, 1, 1, 1]:
        switches = random.choices([0, 1], k=4)

    rounds = 0
    while switches != [1, 1, 1, 1]:
        print(r"""
              

1-------2 
|\     /|
| \   / |
|  \ /  |
|   0   |          
|  / \  |
| /   \ |
|/     \|
3-------4
              

""")    
        if rounds > 0:
            print("Not done yet.")
        print(f"Rounds passed: {rounds}")

        # flipping the switches
        wants_to_flip = flip_switches.get_switches_to_flip()
        rounds += 1
        to_flip = [x-1 for x in wants_to_flip]
        for switch in to_flip:
            if switches[switch] == 0:
                switches[switch] = 1
            else:
                switches[switch] = 0
        
        # the rotation
        amount = random.randint(1, 4)
        amount = amount % len(switches)
        switches = switches[-amount:] + switches[:-amount]

    fewest_rounds = -1
    if rounds < fewest_rounds or fewest_rounds == -1:
        fewest_rounds = rounds
    print(f"Congratulations! You did it! Woohooo! Took ya {rounds} rounds.")
