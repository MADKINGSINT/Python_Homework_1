for X in range (2):
    for Y in range(2):
        for Z in range(2):
            print(not (X or Y or Z) == (not X and not Y and not Z))
            print (X, Y, Z)