n = int(input("Enter number of students: "))
marks = {}

for _ in range(n):
    data = input().split()
    name, scores = data[0], list(map(float, data[1:]))
    marks[name] = scores

query = input("Enter name to get average: ")
print(f"{sum(marks[query]) / len(marks[query]):.2f}")
