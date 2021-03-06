def fat (n):
    fat = 1 
    while (n > 1):
        fat = fat * n
        n -= 1
    return fat

def test_fat0 ():
    assert fat (0)==1