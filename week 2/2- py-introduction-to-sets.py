#py-introduction-to-sets : Calculate the avarges of items present inside a python set

def calculate_average(my_set):
    if len(my_set) == 0:
        return 0
    total = sum(my_set)
    count = len(my_set)
    average = total / count
    return average

if __name__ == "__main__":
    my_set = {10, 20, 30, 40, 50}
    print("Set:", my_set)
    avg = calculate_average(my_set)
    print("Average:", avg)
