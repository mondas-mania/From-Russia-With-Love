from time_system import *
from termcolor import colored


def init_tips():
    tips = open("tips.txt", "r", encoding="utf8")
    tips_list = tips.readlines()
    tips.close()
    new_list = []
    for tips in tips_list:
        tip_text = ""
        comment = False
        for chars in tips:
            if chars == "~":
                comment = True
            if not comment:
                tip_text += chars
        new_list.append(tip_text)

    new_list[:] = [line.strip() for line in new_list]
    return new_list


tips_text_list = init_tips()


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
        print(colored(self.time.display_time(), "red", attrs=["bold"]) + " - from " + self.source.id.capitalize() + " - " + self.text)


def create_tip_from_file(text_id, source, time):
    global tips_text_list
    if text_id == 0:
        return False
    else:
        return tip(tips_text_list[text_id], source, time)

