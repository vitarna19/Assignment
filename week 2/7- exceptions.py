#exceptions : implementing exception handling

def divide_numbers():
    n = int(input("Enter number of test cases: "))

    for _ in range(n):
        try:
            a, b = input("Enter two integers (A B): ").split()
            result = int(a) // int(b)
            print(result)
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)

if __name__ == "__main__":
    divide_numbers()
