def mod3KeyGenerator(seed: int) -> tuple[int, list[int]]:
    round4 = [0] * 16

    found0s = 0
    found1s = 0
    found2s = 0

    while(found0s == 0 or found1s == 0 or found2s == 0):
        found0s = 0
        found1s = 0
        found2s = 0
        
        powerOf2 = 1
        seed = seed + 1

        for i in range(0, 10):
            round4[i] = seed % (powerOf2 * 3) // powerOf2
            
            if (round4[i] == 1):
                found1s = found1s + 1
            elif (round4[i] == 2):
                found2s = found2s + 1
            else:
                found0s = found0s + 1

            powerOf2 = powerOf2 << 1
    
    return (seed, round4)