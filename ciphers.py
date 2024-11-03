from tkinter import *

# Import our encryption algorithms from other files
from caeser import encrypt
from polyalph import encryptVig, encryptGrons
from one_time_pad import encryptOTP

# Define what our dropdowns can say
cipherOptions = [
    "Caeser",
    "Vigenere",
    "Gronsfeld",
    "One-Time Pad"
]

edOptions = [
    "Encrypt",
    "Decrypt"
]

######################
# CALLBACK FUNCTIONS #
######################

def encryptMsg():
    # Get data from text fields and dropdowns
    msg = inputText.get()
    key = keyText.get()

    type = clicked.get()
    edText = edClicked.get()

    # Assign our boolean value for decrypting
    decrypt = False
    if edText == "Decrypt":
        decrypt = True

    # Run the appropriate encryption algorithms based on the dropdown value
    output = ""
    match type:
        case "Caeser":
            output = encrypt(msg, int(key), decrypt)
        case "Vigenere":
            output = encryptVig(msg, key, decrypt)
        case "Gronsfeld":
            output = encryptGrons(msg, key, decrypt)
        case "One-Time Pad":
            output = encryptOTP(msg, key, decrypt)

    outField.delete(0, END)     # Clear the output field
    outField.insert(0, output)  # Display our encrypted value
    
def swap():
    # Store our old values in buffers
    oldInput = inputText.get()
    oldOutput = outField.get()

    # Clear each text field then insert the other value
    inputText.delete(0, END)
    inputText.insert(0, oldOutput)
    outField.delete(0, END)
    outField.insert(0, oldInput)

#################
# UI COMPONENTS #
#################

# Set up our tkinter window
root = Tk()
root.title("Ciphers")
root.geometry("300x250")

# Cipher type dropdown
clicked = StringVar()
clicked.set(cipherOptions[0])

drop = OptionMenu(root, clicked, *cipherOptions)
drop.pack()

# Encrypt/decrypt dropdown
edClicked = StringVar()
edClicked.set(edOptions[0])

edDrop = OptionMenu(root, edClicked, *edOptions)
edDrop.pack()

# Input text field
Label(root, text="Message to encrypt:").pack()
inputText = Entry(root, width=28)
inputText.pack()

# Argument text field (key for caeser, shift for vigenere/gronsfeld, seed for OTP)
Label(root, text="Key/Shift/Seed").pack()
keyText = Entry(root, width=28)
keyText.pack()

# Button to call the encryption function
# I can't be bothered to change what this says based on whether we're encrypting or decrypting
goButton = Button(root, text="Encrypt Message", command=encryptMsg)
goButton.pack()

# Output text field - not a label so we can copy from it
Label(root, text="Result").pack()
outField = Entry(root, width=28)
outField.pack()

# A button to swap the input and output fields
swapButton = Button(root, text="Swap input/output", command=swap)
swapButton.pack()


# Call the main loop on our window so everything works
root.mainloop()
