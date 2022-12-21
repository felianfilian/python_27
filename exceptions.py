

def start():
    total = 0
    names = [{"name": "luigi", "likes": 12,}, { "name": "mario"}, { "name": "peach", "likes": 12,}]
    for name in names:
        try:
            total = total + name["likes"]  # gives an error for mario
        except KeyError:
            pass
    print(total)


