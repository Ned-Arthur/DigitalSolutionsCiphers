# Polyalphabetic cipher
# C_i = (P_i + K_i) mod 26
# Output char = (message char + char of key @ same location) mod 26
# Caeser cipher, but the shift depends on the character in the key

# This implementation doesn't work with spaces because I'm lazy
# That is - a space shouldn't consume one of the key values, but it does

from caeser import encryptChar

offset = 97     # The character code for letter a

# Take a character and convert it to a number to offset by
# Needed for vigenere cipher
def keyToShift(keychar):
    return ord(keychar) - offset

# Vigenere cipher
def encryptVig(text, key, decrypt: bool):
    # Repeat the key as many times as we need to cover the whole message
    while len(key) < len(text):
        key += key
    
    text = text.lower()     # Ignore capitals again
    result = ''

    for i in range(0,len(text)):    # Loop through characters with an index
        char = text[i]      # Get the character at the current index
        if char == ' ':     # Skip spaces
            result += ' '
            continue
        
        # We need the index to get the key value as well as the character
        result += encryptChar(char, keyToShift(key[i]), decrypt)
    
    return result

# Gronsfeld cipher
def encryptGrons(text, key, decrypt: bool):
    skey = f"{key}"     # Make our key a string so we can index into it
                        # If it gets given as a number we cant take the nth digit without first casting to a string
    
    # Same setup as vigenere
    while len(key) < len(text):
        skey += skey
    
    text=text.lower()
    result = ''

    # Same looping method as Vigenere
    for i in range(0, len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
            continue
        
        # Our shift amount is just the current digit in the key as an integer
        result += encryptChar(char, int(skey[i]), decrypt)
    
    return result

def test():
    text = input("Text to encrypt: ")
    key = input("Encryption key: ")

    print(encryptVig(text, key))
