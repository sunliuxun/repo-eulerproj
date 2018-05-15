from euler_util import sqrt

def get_triangle_number_by_i(i):
    return sum(i for i in range(1, i+1))

def get_divisor_amount(n):
    """ Returns the amount of n's divisor in the range [1, n]. """
    r = sqrt(n)
    res = sum(2 for i in range(1, r + 1) if n % i == 0)
    if r ** 2 == n:  # case of n == 16
    	res -= 1
    return res


def find_first_triangle_number_have_over_x_divisors(x):
    i = 1
    while True:
        cur = get_triangle_number_by_i(i)
        divisor_amount = get_divisor_amount(cur)
        if divisor_amount > x:
            return cur
        i += 1
    return -1

if __name__ =="__main__":
    print(find_first_triangle_number_have_over_x_divisors(5)) #28
    print(find_first_triangle_number_have_over_x_divisors(500)) # too much time
    