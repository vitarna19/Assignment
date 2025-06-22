from itertools import groupby

s = input("Enter a string of digits: ")
for key, group in groupby(s):
    print(f"({len(list(group))}, {key})", end=' ')
