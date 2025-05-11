class PokemonCardBinder:
    def __init__(self):
        # In-memory storage for card placements
        # Dictionary to store Pokedex number as key and (page, row, column) as value
        self.binder = {}
        self.max_pokedex_number = 1025
        self.cards_per_page = 64
        self.rows_per_page = 8
        self.columns_per_page = 8

    def add_card(self, pokedex_number):
        # Validate Pokedex number
        if pokedex_number < 1 or pokedex_number > self.max_pokedex_number:
            return f"Error: Pokedex number {pokedex_number} is invalid. Please enter a number between 1 and {self.max_pokedex_number}."

        # Check for duplicate card
        if pokedex_number in self.binder:
            page, row, column = self.binder[pokedex_number]
            return f"Page: {page}, Position: Row {row}, Column {column}, Status: Pokedex #{pokedex_number} already exists in the binder."

        # Calculate page, row, and column for the new card
        total_cards = len(self.binder)
        page = total_cards // self.cards_per_page + 1
        position = total_cards % self.cards_per_page
        row = position // self.columns_per_page + 1
        column = position % self.columns_per_page + 1

        # Add card to the binder
        self.binder[pokedex_number] = (page, row, column)
        return f"Page: {page}, Position: Row {row}, Column {column}, Status: Added Pokedex #{pokedex_number} to binder."

    def reset_binder(self, confirm):
        # Confirm reset
        if confirm.upper() == "CONFIRM":
            self.binder.clear()
            return "The binder reset was successful! All cards have been removed."
        elif confirm.upper() == "EXIT":
            return "Reset canceled. Returning to the Main Menu."
        else:
            return "Invalid input. Type CONFIRM to reset or EXIT to cancel."

    def view_binder(self):
        # Check if binder is empty
        if not self.binder:
            return "The binder is empty.\nTotal cards in binder: 0\n% completion: 0%"

        # Display current binder contents
        result = "Current Binder Contents:\n"
        for pokedex_number, (page, row, column) in sorted(self.binder.items()):
            result += f"Pokedex #{pokedex_number}: Page: {page}, Position: Row {row}, Column {column}\n"

        total_cards = len(self.binder)
        completion_percentage = (total_cards / self.max_pokedex_number) * 100
        result += f"Total cards in binder: {total_cards}\n% completion: {completion_percentage:.2f}%"
        return result

    def exit_program(self):
        total_cards = len(self.binder)
        return f"Thank you for using Pokemon Card Binder Manager! Total cards in binder: {total_cards}"


class PokemonCardBinderManager:
    def __init__(self):
        self.binder = PokemonCardBinder()

    def main_menu(self):
        print("Welcome to Pokemon Card Binder Manager!")
        while True:
            print("\nMain Menu:")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            option = input("Select option: ")

            if option == "1":
                pokedex_number = int(input("Enter Pokedex number: "))
                print(self.binder.add_card(pokedex_number))
            elif option == "2":
                print("WARNING: This will delete ALL Pokemon cards from the binder. This action cannot be undone.")
                confirm = input("Type CONFIRM to reset or 'EXIT' to return to the Main Menu: ")
                print(self.binder.reset_binder(confirm))
            elif option == "3":
                print(self.binder.view_binder())
            elif option == "4":
                print(self.binder.exit_program())
                break
            else:
                print("Invalid option. Please try again.")


# Run the program
if __name__ == "__main__":
    manager = PokemonCardBinderManager()
    manager.main_menu()