def is_prime(x):
    if x < 2:
        return False

    for i in range(2, x):
        if  x % i == 0:
            return False
    return True


def sqrt(x):
    if x < 0:
        raise ValueError("sqrt func input invalid")
	
    i = 1
    
    while i * i <= x:
        i *= 2

    y = 0
    while i > 0:
        if (y + i)**2 <= x:
        	y += i
        i //= 2
    return y