#collections-counter : calculate the total earned amount

from collections import Counter
def calculate_earnings():
    x = int(input("Enter number of items in stock: "))
    sizes = list(map(int, input("Enter available sizes: ").split()))
    n = int(input("Enter number of customers: "))
    stock = Counter(sizes)
    total = 0
    for _ in range(n):
        size, price = map(int, input("Enter requested size and price: ").split())
        if stock[size] > 0:
            total += price
            stock[size] -= 1
    
    print("\nTotal earned:", total)

if __name__ == "__main__":
    calculate_earnings()
