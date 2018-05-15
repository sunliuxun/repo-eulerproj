# brute_force... any improve?
def find_pythagorean_triplet_product(target_sum):
    for a in range(1, target_sum - 3 + 1 + 1):
        for b in range(a + 1, target_sum - 2 + 1 + 1):
            c = target_sum - a - b
            if c > b and a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return -1

if __name__ == "__main__":
    print(find_pythagorean_triplet_product(12)) # 60
    print(find_pythagorean_triplet_product(1000)) # 31875000