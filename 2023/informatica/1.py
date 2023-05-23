# Les 0
def printing():
    print("Hallo , wereld !")
    print(" Hallo ", "hoi", " doei ")
    print(3)
    print(3.0)
    print(2 + 3)
    print(2.0 + 3.0)
    print("bla" + "bla" + "bla")
    print("2 + 3 =", 2 + 3)
    print(2 * 3)
    print(2 ** 3)
    print(7 / 3)
    print(7 // 3)


def greet():
    print(f'Gegroet {input("Wat is je naam? ")}')


def square():
    character = input("Enter a character: ")[0]
    a = f"{character * 6}\n"
    b = f"{character}    {character}\n"
    print(
        a + b + b + b + b + a
    )


def parrot():
    print(f'{input("Wat zeg je? ")*3}')


def length():
    feet = int(input("typ het aantal feet : "))
    inch = int(input("typ het aantal inch : "))
    print(feet*12*2.54+inch*2.54)


def length2():
    cm = int(input("Cm"))
    inch = cm/2.54
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    length()
