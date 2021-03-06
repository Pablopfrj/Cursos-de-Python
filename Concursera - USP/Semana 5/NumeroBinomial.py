def fat (n):
    fat = 1 
    while (n > 1):
        fat = fat * n
        n -= 1
    return fat

def N_binomial(n,k):
     return fat(n)/(fat(k)**fat(n-k))


def fat_unicos ():
    if fat (0) or fat (0):
        print (1)
    if fat (2):
        print (2)