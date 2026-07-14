import sys

def dispay_menu():
    """Prints the main menu and returns the users choice"""
    print("\n" + "="*35)
    print("Vacation & Adventure Tracker")
    print("="*35)
    print("1. Create a new adventure")
    print("2. View saved adventures")
    print("3. Exit")
    print("-"*35)
    return input("Choos an option (1-3): ")

def main():
    """The main loop that keeps the program running"""
    my_adventures = []

    while True:
        choice = dispay_menu()

        if choice == '':
            print("\n>>> Let's plan a new trip!")

            print("[Feature coming soon]")

        elif choice == '2':
            print("\nYour saved adventures:")

            print("[Feature coming soon]")

        elif choice == '3':
            print("\nPacking up... Safe Travels!")
            sys.exit()

        else:
            print("Invalid choice. Please type 1, 2, or 3.")

if __name__ == "__main__":
    main()