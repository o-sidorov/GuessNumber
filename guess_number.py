from numpy import random, mean

"""
Let's play game in which Computer have to find out the number we have guessed.
Initially Computer knows the lower and the higher bounds of the range 
hidden number belongs to.
After every wrong try Computer will be told if predicted number 
is more or less than the one we made.
Thanks to game rules Computer has unlimited tries so it has no chance to loose. 
We just want to know how many tries Computer will take.
"""

        
def guess_number(lo: int=1, hi: int=100, number: int=None, bnr_srch: bool=False) -> int:
    """
    Computer will will try to guess hidden number.
    It has got unlimited tries. 
    The question is how many tries will it use to find out the number
    
    Args:
        lo (int, optional): lower bound of the range the number should belong to. 
        Defaults to 1.
        hi (int, optional): higher bound of the range the number should belong to. 
        Defaults to 100.
        number (int): gessed number.
        Defaults to None (randint(lo, hi+1) will give the number in this case)
        bnr_srch (bool, optional): if True binary search algorythm will be used
        to find out the number, othervice Computer will use randint() function.
        Defaults to False.

    Returns:
        int: number of tries Computer have used to guess the number.
    """
    
    # Check arguments values:
    # lo, hi – int; number – None or int
    if not ((number == None or type(number) == int) and type(lo) == int and type(hi) == int):
        raise ValueError("number, lo, hi values should be integer")
    if lo > hi:
        raise ValueError("lo should be less than hi")
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


def collect_result(func, args_lst: list, key_arg: int, count: int=1) -> list:
    res_lst = []
    for args in args_lst:
        res_lst.append((args[key_arg], func(*args)))
    return res_lst
        
     
if __name__ == '__main__':
    
    def fix_len_num(num: int, length: int) -> str:
        num = str(num)
        return '0'*(length-len(num)) + num 
    
    cnt = 1000000
    lo, hi = 1, 100
    #random.seed(1)
    num_of_tries = [guess_number(lo, hi) for i in range(cnt)]
    avrg_tries = round(mean(num_of_tries))
    best_tries = min(num_of_tries)
    worst_tries = max(num_of_tries)
    tries = {i: num_of_tries.count(i) 
            for i in range(best_tries, worst_tries+1)}
    max_try_val = max(tries.values())
    for item in tries.items():
        print(
            fix_len_num(item[0], 2), '-',
            fix_len_num(item[1], 6), 
            ('=' if item[0] == avrg_tries else '-') * round(item[1]/max_try_val*30)
            )