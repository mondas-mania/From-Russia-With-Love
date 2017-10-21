from time_system import *
from termcolor import colored


class log:
    def __init__(self):
        self.tip = []

    def print_tips(self):
        print(colored("Your notebook:", "red", attrs=["bold", "underline"]))
        for tips in self.tip:
            tips.print_tip()

    def add_tip(self, tip):
        self.tip.append(tip)

    def remove_tip_by_text(self, text):
        for tips in self.tip:
            if tips.text == text:
                self.tip.remove(tips)

    def clear_all(self):
        self.tip = []


class tip:
    def __init__(self, text, source, time):
        self.text = text
        self.source = source
        self.time = time

    def print_tip(self):
        print(colored(self.time.display_time(), "red", attrs=["bold"]) + " - from " + self.source + " - " + self.text)


def create_tip_from_file(text_id, source, time):
    tips = open("tips.txt", "r")
    tips_text_list = tips.readlines()
    tips.close()
    for lines in tips_text_list:
        lines.strip()
    if text_id == 0:
        return False
    else:
        tip_text = ""
        comment = False
        for chars in tips_text_list[text_id]:
            if chars == "~":
                comment = True
            if not comment:
                tip_text += chars

        return tip(tip_text.strip(), source, time)

