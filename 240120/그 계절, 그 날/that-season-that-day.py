Y, M, D = map(int, input().split())


def sol():

    days31 = [1, 3, 5, 7, 8, 10, 12]

    leap = False

    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                leap = True

    if not leap and (M == 2 and D == 29):
        return -1

    if M not in days31 and D >= 31:
        return -1

    if M >= 3 and M <= 5:
        return "Spring"

    if M >= 6 and M <= 8:
        return "Summer"

    if M >= 9 and M <= 11:
        return "Fall"

    if M == 12 or M <= 2:
        return "Winter"


    return -1


print(sol())