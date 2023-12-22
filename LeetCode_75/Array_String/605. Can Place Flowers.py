from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    i = 0
    n_flowerbed = len(flowerbed)

    if n_flowerbed > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
    elif n_flowerbed == 1 and flowerbed[0] == 0:
        return True
    
    
    while i < (n_flowerbed - 1):
        if (flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0) and (flowerbed[i] == 0):
            flowerbed[i] = 1
            n -= 1
        i += 1
    
    if n_flowerbed > 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1
    
    return n == 0

        
print(canPlaceFlowers(flowerbed = [0,0,1,0,1], n = 1))