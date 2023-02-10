def rotate(word, rotation):
    alphabet = list(map(chr, range(97, 123))) + list(map(chr, range(97, 123)))
    rotation = rotation % 26
    encoded = []
    for i in word:
        if i.isupper():
            encoded.append(alphabet[alphabet.index(i.lower()) + rotation].upper())
        elif i.islower():
            encoded.append(alphabet[alphabet.index(i.lower()) + rotation])
        else:
            encoded.append(i)
    return ''.join(encoded)


if __name__ == "__main__":
    print(rotate(input("Enter a word: "), int(input("Enter rotation number: "))))
