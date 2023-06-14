# Defines instrument class
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

    def __str__(self):
        info = f"Material: {self.material}\nFamily: {self.family}\nSize: {self.size}"
        return info

    def playScale(self):
        msg = "You can't play a scale on a drum kit, silly!"
        print(msg)


def getMsg():

    def inst_msg():
        inst = Instrument()
        inst.tuning = scale
        inst.playScale()

    def play_again():
        again = input("Would you like to play again? (Y/N)\n").lower()
        if again == 'y':
            print("Great!\n")
            getMsg()
        elif again == 'n':
            print("Thanks for playing!")
        else:
            print(
                "Sorry! Type 'Y' if you'd like to play again, or 'N' if you're done playing.")

    inst = input("What instrument are you playing a scale with?\n").lower()
    if inst == "drum":
        drum = Drum()
        drum.playScale()
        play_again()
    else:
        scale = input("What scale would you like to play?\n")
        if scale == '':
            go = True
            while go:
                scale = input(
                    "Oops, looks like you left it blank. Try again.\nWhat scale would you like to play?\n")
                if scale == '' or scale.isspace():
                    go = True
                else:
                    go = False
                    inst_msg()
                    play_again()
        else:
            inst_msg()
            play_again()


if __name__ == "__main__":
    getMsg()
