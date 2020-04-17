from inputs import numberInput, yesNoInput, optionsInput

loader = optionsInput("Type of station?", ["Loader", "Unloader"])
trains = numberInput("Number of cargo wagons: ")
stack = numberInput("Stack size of the item: ")

loader = True if loader == "loader" else False


if loader:
    num = trains * 40 * stack
    print('Set the condition to "Enable/disable" "[item] > ' + str(num))
else:
    sides = yesNoInput("Do you unload chests from both sides of the train?")
    s = 2 if sides else 1
    num = (trains * 6 * 48 * stack * s) - (trains * 40 * stack)
    print('Set the condition to "Enable/disable" "[item] < ' + str(num))
