# Class Definitions
class Instrument:
    material = None
    family = None
    tuning = None
    size = None

    def playScale(self):
        msg = f"You played the scale in {self.tuning}!"
        print(msg)


class Drum(Instrument):
    material = 'wood'
    family = 'percussion'
    size = 'large'

    def playScale(self):
        msg = "You can't play a scale on a drum kit, silly!"
        print(msg)


# Function to get non-empty input from user
def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Oops, looks like you left it blank. Try again.")


# Main function
def main():
    while True:
        inst = get_non_empty_input(
            "What instrument are you playing a scale with?\n").lower()

        if inst == "drum":
            drum = Drum()
            drum.playScale()
        else:
            scale = get_non_empty_input("What scale would you like to play?\n")
            instrument = Instrument()
            instrument.tuning = scale
            instrument.playScale()

        # Ask to play again
        again = input("Would you like to play again? (Y/N)\n").lower()
        if again == 'n':
            print("Thanks for playing!")
            break
        elif again != 'y':
            print(
                "Sorry! Type 'Y' if you'd like to play again, or 'N' if you're done playing.")


if __name__ == "__main__":
    main()
