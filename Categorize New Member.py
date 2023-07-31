def open_or_senior(data):
    ls = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            ls.append("Senior")
        else:
            ls.append("Open")
    return ls
