def find_sum(n):
    x = 2 ** n
    res = sum(int(c) for c in str(x))
    return res

if __name__ == "__main__":
    print(find_sum(15))  # 26
    print(find_sum(1000)) # 1366
    