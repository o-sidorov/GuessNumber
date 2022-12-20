from numpy import random, mean

"""
Let's play game in which Computer finds out the number we have guessed.
Initially Computer knows the lower and the upper bounds of the range 
hidden number belongs to.
After every wrong try Computer will be told if predicted number 
is more or less than the one we made.
Thanks to game rules Computer has unlimited tries so it has no chance to loose. 
The ustion is how many tries Computer will take.
"""

def guess_number(lo: int=1, hi: int=100, number: int=None, bnr_srch: bool=True) -> int:
    """
    Computer will try to guess hidden number.
    It has got unlimited tries. 
    The result is how many tries will it use to find out the number
    
    Args:
        lo (int, optional): lower bound of the range the number should belong to. 
        Defaults to 1.
        hi (int, optional): higher bound of the range the number should belong to. 
        Defaults to 100.
        number (int): gessed number.
        Defaults to None (randint(lo, hi+1) will give the number in this case)
        bnr_srch (bool, optional): if True binary search algorythm will be used
        to search the number, othervice Computer will use randint() function.
        Defaults to True.

    Returns:
        int: number of tries Computer have used to guess the number.
    """
    
    # Check arguments values:
    # lo, hi – int; number – None or int
    if not ((number == None or type(number) == int) and type(lo) == int and type(hi) == int):
        raise ValueError("number, lo, hi values should be integer")
    if lo > hi:
        raise ValueError("lo can't be more than hi")
    if not number:
        number = random.randint(lo, hi+1)
    # number value should be in range [lo, hi]
    if not lo <= number <= hi:
        raise ValueError("number should be in range from lo to hi")
    
    # Now let Computer guess the number
    count = 1
    while True:
        if bnr_srch:
            guess = (lo+hi) // 2
        else:
            guess = random.randint(lo, hi+1)
            
        if guess == number:
            return count
        elif guess < number:
            lo = guess+1
        else:
            hi = guess-1
        count += 1