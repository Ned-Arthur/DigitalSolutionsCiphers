offset = 97     # The character code for letter 'a'

def encryptChar(char, shift, decrypt: bool):
    if decrypt:
        return chr((ord(char) - shift - offset) % 26 + offset) # If we're decrypting we subtract the shift amount

    return chr((ord(char) + shift - offset) % 26 + offset)
    # (character code + shift - offset) = new character starting at 0
    # ... % 26                          = remainder after divide 26, i.e. new
    #                                       character from 0 to 25
    # + offset                          = bring 0-25 num back to character code

def encrypt(text, shift, decrypt: bool):
    lowerText = text.lower()    # Don't bother with capitals to make it easier
    result = ''
    for c in lowerText:     # loop through characters
        if c == ' ':        # Ignore spaces
            result += ' '
        else:
            result += encryptChar(c, shift, decrypt)    # Append the encrypted character to our result output
    
    return result

def test():
    text = input("Text to encrypt: ")
    shift = int(input("Shift amount: "))

    print(encrypt(text, shift))
