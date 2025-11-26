hour = 0
minute = 0
second = 0

def show():
    print(f"{hour} : {minute} : {second}")


def time():
    global hour
    global minute
    global second

    
    second = second + 1
    if second == 60:
        second = 0
        minute = minute + 1
        if minute == 60:
            minute = 0
            hour = hour + 1
