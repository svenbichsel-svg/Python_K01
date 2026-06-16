 import string

    for zeile in range(8, 0, -1):
        for spalte in string.ascii_lowercase[:8]:
            print(spalte + str(zeile), end=" ")
        print()
