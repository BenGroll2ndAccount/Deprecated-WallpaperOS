def isValidDate(input : str):
    if not len(input.split(".")) == 3:
        return False
    if len(input.split(".")[0]) != 2:
        return False
    if len(input.split(".")[1]) != 2:
        return False
    if len(input.split(".")[2]) != 4:
        return False
    if int(input.split(".")[0]) > 31 or int(input.split(".")[0]) < 1:
        return False
    if int(input.split(".")[1]) > 12 or int(input.split(".")[1]) < 1:
        return False
    return True

