#incorrect-regex : regex based problem statement

import re
def check_regex_validity():
    n = int(input("Enter number of test cases: "))
    for _ in range(n):
        pattern = input("Enter regex pattern: ")
        try:
            re.compile(pattern)
            print(True)
        except re.error:
            print(False)

if __name__ == "__main__":
    check_regex_validity()
