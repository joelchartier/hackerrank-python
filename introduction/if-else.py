if __name__ == '__main__':

    n = int(input())
    value = ""

    if n % 2 == 1:
        value = "Weird"
    elif n % 2 == 0:
        if n >= 2 and n <= 5:
            value = "Not Weird"
        elif n >= 6 and n <= 20:
            value = "Weird"
        elif n > 20:
            value = "Not Weird"

    print(value)