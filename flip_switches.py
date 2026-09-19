def get_switches_to_flip(): 
    while True:
        raw = input("Which switches do you want to flip?\n")
        
        try:
            to_flip = [int(x) for x in raw.split()]
        except ValueError:
            print("Please only enter numbers, separated by spaces. Did I not explain it properly?")
            continue
        
        if len(to_flip) > 4:
            print("Max 4 switches, dummy.")
            continue
        
        if not all(1 <= item <= 4 for item in to_flip):
            print("There are only 4 switches what are you pulling  ?")
            continue
        
        if len(set(to_flip)) != len(to_flip):
            print("Don't enter the same switch twice. Won't tell u again pal.")
            continue
        
        return to_flip
