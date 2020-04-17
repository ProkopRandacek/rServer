def numberInput(text):
    while True:
        i = input(text)
        if i.isdigit():
            break
        else:
            print("You did not enter a number")
    return int(i)


def boolInput(text):
    while True:
        i = input(text + "[" + options[0] + "/" + opitions[1] + "] ")
        if i.isdigit():
            break
        else:
            print("You did not enter a valid option")
    return int(i)


def optionsInput(text, options):
    options = [i.lower() for i in options]
    while True:
        i = input(text + f" [{'/'.join(options)}] ").lower()
        if i in options:
            break
        elif i in [o[0] for o in options]:
            for o in options:
                if i == o[0]:
                    i = o
            break
        else:
            print("You did not enter a valid option")
    return i


def yesNoInput(text):
    while True:
        i = input(text + " [Y/n] ").lower()
        if i in ["yes", "y", "no", "n", ""]:
            break
        else:
            print("You did not enter a valid answer")
    return True if i in ["yes", "y"] else False
