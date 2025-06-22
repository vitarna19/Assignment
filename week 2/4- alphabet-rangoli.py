#alphabet-rangoli : pattern printing with the help of alphabets

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = '-'.join(alphabet[size-1:i:-1])
        right = '-'.join(alphabet[i:size])
        full_line = (left + '-' + right) if left else right
        lines.append(full_line.center(4 * size - 3, '-'))

    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == "__main__":
    n = int(input("Enter size (1-26): "))
    print()
    print_rangoli(n)

