def initialize_fruits(fruit_names, quantities, fruit1, fruit2, fruit3, fruit4, fruit5, qty1, qty2, qty3, qty4, qty5):
    fruit_names.extend([fruit1, fruit2, fruit3, fruit4, fruit5])
    quantities.extend([qty1, qty2, qty3, qty4, qty5])

def run():
    fruit_names = []
    quantities = []
    initialize_fruits(fruit_names, quantities, "Apple", "Banana", "Cherry", "Date", "Elderberry", 10, 20, 30, 40, 50)

    try:
        while True:
            print("(A)dd fruits")
            print("(R)emove fruits")
            print("(T)ransfer fruits")
            print("E(X)it")
            command = input("Command: ").upper()

            if command == "A":
                fruit = input("Which fruit do you want to add to? ")
                amount = int(input("How many do you want to add? "))
                if fruit in fruit_names:
                    index = fruit_names.index(fruit)
                    quantities[index] += amount
                    print(f"New quantity for {fruit}: {quantities[index]}")
                continue

            if command == "R":
                fruit = input("Which fruit do you want to remove from? ")
                amount = int(input("How many do you want to remove? "))
                if fruit in fruit_names:
                    index = fruit_names.index(fruit)
                    quantities[index] -= amount
                    print(f"New quantity for {fruit}: {quantities[index]}")
                continue

            if command == "T":
                from_fruit = input("From which fruit do you want to transfer? ")
                to_fruit = input("To which fruit do you want to transfer? ")
                amount = int(input("How many do you want to transfer? "))
                if from_fruit in fruit_names and to_fruit in fruit_names:
                    from_index = fruit_names.index(from_fruit)
                    to_index = fruit_names.index(to_fruit)
                    quantities[from_index] -= amount
                    quantities[to_index] += amount
                    print(f"New quantity for {from_fruit}: {quantities[from_index]}")
                    print(f"New quantity for {to_fruit}: {quantities[to_index]}")
                continue

            if command == "X":
                return 0

            return -1

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return -1

def main():
    error = run()
    if error < 0:
        print("Error")
    else:
        print("Good Bye")

if __name__ == "__main__":
    main()
