from termcolor import colored
from time import *


class log:
    def __init__(self):
        self.tip = []

    def print_tips(self):
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
        print(colored(self.time.display_time, "red", attrs=["bold"]) + " - from " + self.source + " - " + self.text)


time = basic_time(13, 49)
time.display_time()