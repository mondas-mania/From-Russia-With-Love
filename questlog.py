from termcolor import colored

class log:
    def __init__(self):
        self.tip = []

    def print__tips(self):
        print(colored("Your notebook:", "red", attrs=["bold", "underline"]))
        for tips in self.tip:
            tips.print_tip()

    def add_tip(self, tip):
        self.tip.append(tip)


class tip:
    def __init__(self, text, source, time):
        self.text = text
        self.source = source
        self.time = time

    def print_tip(self):
        print(colored(self.time, "red", attrs=["bold"]) + " - from " + self.source + " - " + self.text)


tip1 = tip("You should play the game", "David", "13:59")
tip2 = tip("or just go home, idk", "David", "14:03")
qlog = log()
qlog.add_tip(tip1)
qlog.add_tip(tip2)
