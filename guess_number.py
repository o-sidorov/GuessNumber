from numpy import random, mean

"""
Let's play game in which Computer finds out the number we have guessed.
Initially Computer knows the lower and the upper bounds of the range 
hidden number belongs to.
After every wrong try Computer will be told if predicted number 
is more or less than the one we made.
Thanks to game rules Computer has unlimited tries so it has no chance to loose. 
We just want to know how many tries Computer will take.
"""
def print_tabs(*args, tabs: tuple=None):
    for arg, tab in zip(args, tabs):
        print(arg, ' '*(tab-len(str(arg))), sep='', end='')
    print()

def average_int_result(func, repeat: int=1000, print_chart: bool=True):
    def dec_func(*args, **kwargs):
        results = [func(*args, **kwargs) for i in range(repeat)]
        avrg_res = round(mean(results))
        
        if print_chart:
            # Printing a simple chart
            min_res = min(results) # lower bound of chart value axis
            max_res = max(results) # upper bound of chart value axis
            # Creating a dictionary:
            # keys are results returned by func();
            # values are numbers of times each result was returned.
            results = {i: results.count(i) 
                        for i in range(min_res, max_res+1)}
            max_val = max(results.values()) # count of the most frequent result
            
            for result in results.items():
                chart_ch = '=' if result[0] == avrg_res else '-'
                chart_bar = chart_ch * round(result[1]/max_val*50)
                print_tabs(result[0], '-', result[1], chart_bar, tabs=(3,2,5,0))
                
        return avrg_res
    return dec_func

def guess_number(lo: int=1, hi: int=100, number: int=None, bnr_srch: bool=True) -> int:
    """
    Computer will try to guess hidden number.
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


#if __name__ == '__main__':
''' guess_number = average_int_result(guess_number, repeat=100)
    for hi in [10**i for i in range(2,6)]:
        print(f"\n[1; {hi}]")
        print(f"Average number of tries is {guess_number(1, hi)}")'''