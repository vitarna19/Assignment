#merge-the-tools : Split a string into equal parts of length and Convert each parts by removing any subsequent occurrences of non-distinct

def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        part = string[i:i+k]
        result = ""
        for char in part:
            if char not in result:
                result += char
        print(result)

if __name__ == "__main__":
    s = input("Enter the string: ")
    k = int(input("Enter the part length (k): "))
    print("\nOutput:")
    merge_the_tools(s, k)
