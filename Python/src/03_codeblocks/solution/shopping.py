def initialize_fruits(fruit_names, quantities, fruits_with_quantities):
    for fruit, quantity in fruits_with_quantities.items():
        fruit_names.append(fruit)
        quantities.append(quantity)

def display_inventory(fruit_names, quantities):
    print("Current inventory:")
    for fruit, quantity in zip(fruit_names, quantities):
        print(f"{fruit}: {quantity}")
    print()

def add_fruits(fruit_names, quantities):
    fruit = input("Which fruit do you want to add to? ")
    if fruit not in fruit_names:
        print(f"{fruit} is not in the list.")
        return
    try:
        amount = int(input("How many do you want to add? "))
        index = fruit_names.index(fruit)
        quantities[index] += amount
        print(f"New quantity for {fruit}: {quantities[index]}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def remove_fruits(fruit_names, quantities):
    fruit = input("Which fruit do you want to remove from? ")
    if fruit not in fruit_names:
        print(f"{fruit} is not in the list.")
        return
    try:
        amount = int(input("How many do you want to remove? "))
        index = fruit_names.index(fruit)
        quantities[index] -= amount
        print(f"New quantity for {fruit}: {quantities[index]}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def transfer_fruits(fruit_names, quantities):
    from_fruit = input("From which fruit do you want to transfer? ")
    to_fruit = input("To which fruit do you want to transfer? ")
    if from_fruit not in fruit_names or to_fruit not in fruit_names:
        print("One or both fruits are not in the list.")
        return
    try:
        amount = int(input("How many do you want to transfer? "))
        from_index = fruit_names.index(from_fruit)
        to_index = fruit_names.index(to_fruit)
        quantities[from_index] -= amount
        quantities[to_index] += amount
        print(f"New quantity for {from_fruit}: {quantities[from_index]}")
        print(f"New quantity for {to_fruit}: {quantities[to_index]}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def display_menu():
    print("(A)dd fruits")
    print("(R)emove fruits")
    print("(T)ransfer fruits")
    print("E(X)it")

def run():
    fruit_names = []
    quantities = []
    fruits_with_quantities = {
        "Apple": 10,
        "Banana": 20,
        "Cherry": 30,
        "Date": 40,
        "Elderberry": 50
    }
    initialize_fruits(fruit_names, quantities, fruits_with_quantities)
    display_inventory(fruit_names, quantities)

    try:
        while True:
            display_menu()
            command = input("Command: ").upper()

            if command == "A":
                add_fruits(fruit_names, quantities)
            elif command == "R":
                remove_fruits(fruit_names, quantities)
            elif command == "T":
                transfer_fruits(fruit_names, quantities)
            elif command == "X":
                print("Good Bye")
                return 0
            else:
                print("Invalid command. Please try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return -1

def main():
    error = run()
    if error < 0:
        print("Error")

if __name__ == "__main__":
    main()
