from euler_util import is_prime

def find_nth_prime(n):
    cur = 2 # init: 第一个prime是2
    cnt = 1 # init

    while cnt <= n:
        if is_prime(cur) and cnt == n: # 退出条件先写
            return cur   
        if is_prime(cur):            
            cnt += 1    
        cur += 1

    return -1
     # 这种需要loop从0开始的，用while



if __name__ == "__main__":
    print(find_nth_prime(6)) # 13
    print(find_nth_prime(10001)) # too much time!