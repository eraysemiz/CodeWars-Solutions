def rgb(r, g, b):
    values = [r, g, b]
    index = 0
    for i in values:
        if i > 255:
            values[index] = 255
        elif i < 0:
            values[index] = 0

        index += 1
    return f"{values[0]:02X}{values[1]:02X}{values[2]:02X}"
