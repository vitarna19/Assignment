#py-set-discard-remove-pop : task based on discard(),remove() & pop()

def perform_operations():
    n = int(input("Enter the number of elements in the set: "))
    s = set(map(int, input("Enter the elements (space-separated): ").split()))
    num_commands = int(input("Enter the number of commands: "))

    print("\n--- Executing Commands ---")
    for _ in range(num_commands):
        command = input().strip().split()

        if command[0] == "pop":
            if s:
                popped = s.pop()
                print(f"pop(): Removed {popped}")
            else:
                print("pop(): Set is empty, cannot pop.")

        elif command[0] == "remove":
            val = int(command[1])
            if val in s:
                s.remove(val)
                print(f"remove({val}): Removed {val}")
            else:
                print(f"remove({val}): Element not found in set (raises error)")
                raise KeyError(f"{val} not in set")

        elif command[0] == "discard":
            val = int(command[1])
            if val in s:
                s.discard(val)
                print(f"discard({val}): Discarded {val}")
            else:
                print(f"discard({val}): Element not in set, nothing happened")

    print("\nFinal Set:", s)
    print("Sum of remaining elements in the set:", sum(s))

if __name__ == "__main__":
    perform_operations()
