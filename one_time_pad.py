import random
import string

from polyalph import encryptVig

# Generate a random key the length we need
def generateKey(length, seed):
    random.seed(seed)   # Set the seed of our random generator
                        # The same seed will always produce the same output
    key = ""
    for i in range (0, length):
        key += random.choice(string.printable)      # Append a random character to our key string

    return key

def encryptOTP(text, seed, decrypt: bool):
    # Make our key
    key = generateKey(len(text), seed)

    # Now we've got a string of characters to use as our key...
    # (Literally just a vigener cipher now, so I didn't bother implementing it again)
    result = encryptVig(text, key, decrypt)

    return result
