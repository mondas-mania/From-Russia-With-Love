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


class tip:
    def __init__(self, text, source, time):
        self.text = text
        self.source = source
        self.time = time

    def print_tip(self):
        print(colored(self.time, "red", attrs=["bold"]) + " - from " + self.source + " - " + self.text)


class basic_time:
    def __init__(self, hrs, mins):
        self.hours = hrs
        self.mins = mins

    def display_time(self):
        if len(str(self.mins)) == 1:
            time = str(self.hours) + ":0" + str(self.mins)
        else:
            time = str(self.hours) + ":" + str(self.mins)
        return time

    def incr_time(self, hrs, mins):
        self.mins += mins
        if self.mins >= 60:
            self.hours += self.mins // 60
            self.mins = self.mins % 60

        self.hours += hrs
        if self.hours >= 24:
            self.hours = self.hours % 24


