def main():
    og_tekst = input("Ievadi tekstu : ")
    shorten(og_tekst)

def shorten(og_tekst):    
    new_teksts = ""
    vowls = "aeoiuAEOIU"

    for letter in og_tekst:
        if letter not in vowls:
            new_teksts += letter

    return new_teksts


if __name__ == "__main__":
    main()