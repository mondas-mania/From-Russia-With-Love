class basic_time:
    def __init__(self, hrs, mins):
        self.hours = hrs
        self.mins = mins

    def display_time(self):
        if len(str(int(self.mins))) == 1:
            time = str(int(self.hours)) + ":0" + str(int(self.mins))
        else:
            time = str(int(self.hours)) + ":" + str(int(self.mins))
        return time

    def incr_time(self, hrs, mins):
        self.mins += mins
        if self.mins >= 60:
            self.hours += self.mins // 60
            self.mins = self.mins % 60

        self.hours += hrs
        if self.hours >= 24:
            self.hours = self.hours % 24

    def decr_time(self, hrs, mins):
        self.mins -= mins
        if self.mins < 0:
            self.hours += self.mins // 60
            self.mins = self.mins % 60

        self.hours -= hrs
        if self.hours < 0:
            self.hours = self.hours % 24


def larger_time(time1, time2):
    if time1.hours > time2.hours:
        return time1
    elif time1.hours < time2.hours:
        return time2
    else:
        if time1.mins > time2.mins:
            return time1
        elif time1.mins < time2.mins:
            return time2
        else:
            return False


def diff_times(time1, time2):
    larger = larger_time(time1, time2)
    if not larger:
        return basic_time(0, 0)
    else:
        larger = get_time_from_str(larger.display_time())

    if larger.display_time() == time1.display_time():
        smaller = time2
    else:
        smaller = time1

    larger.decr_time(smaller.hours, smaller.mins)
    return larger


def get_time_from_str(str):
    str = str.strip()
    section = "h"
    hrs = ""
    mins = ""
    for chars in str:
        if section == "h" and chars != ":":
            hrs += chars

        if section == "m":
            mins += chars

        if chars == ":":
            section = "m"

    return basic_time(int(hrs), int(mins))


#time1 = get_time_from_str("  11:49  \n")
#time2 = basic_time(11, 46)
#diff = diff_times(time1, time2)
#print(diff.display_time())
