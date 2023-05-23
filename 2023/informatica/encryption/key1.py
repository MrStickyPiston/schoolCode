import random
import string


def generate_key():
    """Generates a random key that contain all printables ONCE"""
    characters = string.printable
    key = "".join(random.sample(characters, len(characters)))
    return key


def check_key(key):
    """Check a key if it contains all printables ONCE"""
    characters = string.printable
    if len(key) == len(characters):
        for i in key:
            if key.count(i) > 1:
                return False
        return True
    return False


def encrypt(text: str, key: str = "None"):
    """Encrypt using a key.
    text: the text to encrypt
    key: the key to use
    returns the encrypted message and the key used."""
    characters = string.printable

    while check_key(key) is False:
        key = generate_key()
        print(f"Generating a new key: {repr(key)}")

    encrypted = ""
    for i in range(len(text)):
        # print(key[characters.index(text[i])])  DEBUG logging
        encrypted += key[characters.index(text[i])]
    return [encrypted, key]


def decrypt(text: str, key: str):
    """Decrypts text with a key
    text: the text to decrypt
    key: the key to use
    returns the decrypted message"""
    characters = string.printable

    if not check_key(key):
        print("Error: invalid key")

    decrypted = ""
    for i in range(len(text)):
        # print(characters[key.index(text[i])]) DEBUG logging
        decrypted += characters[key.index(text[i])]
    return [decrypted, key]


if __name__ == "__main__":
    """Some examples of encryption"""
    print(decrypt("""0s1l
;Ynv)
;3ss1;vYX;9
lX""",
                  '2z_\x0bjS!]M^9Q\\3l#NBY?<\x0c\n(sn&1vX)xm:fCW$\r\t=o@e8cg0UTt|Fq\'hwk-K~E dVbDi}%ZG56I[/u.yLPJ,p>*{A"HOa4;R`+7r')[
              0])
    print(encrypt(
        "Lorem ipsum dolor sit amet",
        '2z_\x0bjS!]M^9Q\\3l#NBY?<\x0c\n(sn&1vX)xm:fCW$\r\t=o@e8cg0UTt|Fq\'hwk-K~E dVbDi}%ZG56I[/u.yLPJ,p>*{A"HOa4;R`+7r')[
              0])
