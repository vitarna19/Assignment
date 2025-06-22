from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))
a_count = sum(1 for combo in all_combinations if 'a' in combo)
print(f"{a_count / len(all_combinations):.4f}")
