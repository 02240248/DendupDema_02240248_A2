import random
from DendupDema_02240248_A2_PB import PokemonCardBinder

class GuessNumberGame:
    """A simple number guessing game."""
    def __init__(self, low=1, high=10):
        self.low = low
        self.high = high
        self.secret_number = random.randint(low, high)

    def play(self):
        attempts = 0
        while True:
            try:
                guess = int(input(f"Guess a number between {self.low} and {self.high}: "))
                attempts += 1
                if guess < self.low or guess > self.high:
                    print("Out of range! Try again.")
                elif guess < self.secret_number:
                    print("Too low!")
                elif guess > self.secret_number:
                    print("Too high!")
                else:
                    print(f"Correct! You guessed it in {attempts} attempts.")
                    return max(0, (self.high - self.low + 1) - attempts)
            except ValueError:
                print("Invalid input! Please enter a number.")

class RockPaperScissors:
    """A simple Rock-Paper-Scissors game."""
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def play(self):
        score = 0
        while True:
            user = input("Choose rock, paper, or scissors: ").lower()
            computer = random.choice(self.choices)
            print(f"Computer chose: {computer}")

            if user == computer:
                print("It's a tie!")
            elif (user == "rock" and computer == "scissors") or \
                 (user == "paper" and computer == "rock") or \
                 (user == "scissors" and computer == "paper"):
                print("You win!")
                score += 1
            else:
                print("You lose!")

            if input("Play again? (yes/no): ").lower() != "yes":
                return score

class TriviaGame:
    """A simple trivia game."""
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A. Paris", "B. London", "C. Berlin"], "answer": "A"},
            {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic", "B. Indian", "C. Pacific"], "answer": "C"}
        ]

    def play(self):
        score = 0
        for q in self.questions:
            print(f"\n{q['question']}")
            for opt in q['options']:
                print(opt)
            user_answer = input("Your answer (A/B/C): ").strip().upper()
            if user_answer == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q['answer']}")
        print(f"\nYour score: {score}/{len(self.questions)}")
        return score


class OverallScore:
    """Tracks scores for all games."""
    def __init__(self):
        self.scores = {}

    def update_score(self, game, score):
        self.scores[game] = self.scores.get(game, 0) + score

    def display_score(self):
        print("\nScores:")
        for game, score in self.scores.items():
            print(f"{game}: {score}")
        print(f"Total: {sum(self.scores.values())}")



class PokemonManagerWrapper:
    def __init__(self, binder, tracker):
        self.binder = binder
        self.tracker = tracker

    def manage(self):
        print("---Welcome to Pokemon Card Binder Manager!---")
        while True:
            print("\nMain Menu:\n1. Add Pokemon card\n2. Reset binder\n3. View current placements\n4. Exit")
            choice = input("Select option: ")
            if choice == "1":
                try:
                    number = int(input("Enter Pokedex number: "))
                    msg = self.binder.add_card(number)
                    if "Added" in msg:
                        self.tracker.add_score("Pokemon", 1)
                    print(msg)
                except ValueError:
                    print("Invalid number.")
            elif choice == "2":
                print("WARNING: This will delete ALL cards. Type 'CONFIRM' to reset or 'EXIT' to cancel.")
                confirm = input("Type here: ")
                print(self.binder.reset_binder(confirm))
            elif choice == "3":
                print(self.binder.view_binder())
            elif choice == "4":
                print(self.binder.exit_program())
                break
            else:
                print("Invalid input.")

class ScoreTracker:
    """Tracks scores for different games."""
    def __init__(self):
        self.scores = {}

    def add_score(self, game, score):
        self.scores[game] = self.scores.get(game, 0) + score

    def display_score(self):
        print("\nScores:")
        for game, score in self.scores.items():
            print(f"{game}: {score}")
        print(f"Total: {sum(self.scores.values())}")


def main():
    binder = PokemonCardBinder()
    tracker = ScoreTracker()

    while True:
        print("\nSelect a function (0-5):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall score")
        print("0. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            score = GuessNumberGame().play()
            tracker.add_score("Guess", score)
        elif choice == "2":
            score = RockPaperScissors().play()
            tracker.add_score("RPS", score)
        elif choice == "3":
            score = TriviaGame().play()
            tracker.add_score("Trivia", score)
        elif choice == "4":
            PokemonManagerWrapper(binder, tracker).manage()
        elif choice == "5":
            tracker.display_score()
        elif choice == "0":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 5.")

if __name__ == "__main__":
    main()