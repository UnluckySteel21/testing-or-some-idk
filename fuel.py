def main():
    fraction = input("Fractioin : ")
    a, b = convert(fraction)
    gauge(a, b)


def convert(fraction):
    try:
        converted = fraction.split("/")
        fractionTop = int(converted[0])
        fractionBottom = int(converted[1])
        return fractionTop, fractionBottom
    except:
        main()

def gauge(fractionTop, fractionBottom):
    if fractionTop <= fractionBottom:
        if fractionTop > 0:
            percentage = round(fractionTop/fractionBottom*100, 2)
            if percentage <= 1:
                return "E"
            if percentage >= 99:
                return "F"
            percentage = str(percentage) + "%"
            print(percentage)
            return percentage
        else:
            raise ZeroDivisionError("Cant devide with 0")
    else:
        raise ValueError("Top cant be bigger then bottom")


if __name__ == "__main__":
    main()