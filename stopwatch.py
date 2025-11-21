import time

class waktu:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def show():
        print(f"{hour} : {minute} : {second}")
        time.sleep(1)


    def time():
        second = second + 1
        if second == 60:
            minute = minute + 1
            if minute == 60:
                hour = hour + 1