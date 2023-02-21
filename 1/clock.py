def to_text(hours, minutes):
    Numbers = [
        "",
        "Een",
        "Twee",
        "Drie",
        "Vier",
        "Vijf",
        "Zes",
        "Zeven",
        "Acht",
        "Negen",
        "Tien",
        "Elf",
        "Twaalf",
        "Dertien",
        "Veertien",
        "Kwart",
        "Zestien",
        "Zeventien",
        "Achttien",
        "Negentien",
        "Twintig"
    ]

    hours %= 12
    if 20 >= minutes >= 0:
        print(f"{Numbers[minutes]} over {Numbers[hours]}")

    if 40 >= minutes >= 20:
        if minutes > 30:
            print(f"{Numbers[minutes - 30]} over half {Numbers[hours]}")
        elif minutes < 30:
            print(f"{Numbers[30 - minutes]} voor half {Numbers[hours]}")
        else:
            print(f"Half {Numbers[hours]}")

    if 60 > minutes >= 40:
        print(f"{Numbers[60 - minutes]} voor {Numbers[hours + 1]}")


if __name__ == "__main__":
    to_text(20, 45)
