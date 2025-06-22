n = int(input("Enter number of elements: "))
t = tuple(map(int, input("Enter space-separated numbers: ").split()))
print(hash(t))
