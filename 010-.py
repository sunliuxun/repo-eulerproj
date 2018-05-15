from euler_util import is_prime

def find_prime_under_ceiling_sum(ceiling):
    cur = 0
    res = 0
    while cur < ceiling:
        if is_prime(cur):
            res += cur
        cur += 1
    return res


if __name__ == "__main__":
    print(find_prime_under_ceiling_sum(10)) # 17
    print(find_prime_under_ceiling_sum(2000000)) # too much time!