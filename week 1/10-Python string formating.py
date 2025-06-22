def print_formatted(n):
    width = len(bin(n)[2:])
    for i in range(1, n + 1):
        print(f"{i:{width}d} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")

n = int(input("Enter a number: "))
print_formatted(n)
