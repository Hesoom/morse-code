MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':'/'}

REVERSE_MORSE_CODE_DICT = {v:k for k,v in MORSE_CODE_DICT.items()}

def encrypt(text):
    encrypted_text = ""
    text = text.upper()
    for letter in text:
        encrypted_text += MORSE_CODE_DICT.get(letter,'?') + " "
    return encrypted_text.strip()
       
def decrypt(morse_code):
    decoded_text  = ""
    words = morse_code.split(" / ")
    for word in words:
        #Chop the word in to seperate letters to translate letter by letter
        letters = word.split()
        for letter_code in letters:
            decoded_text += REVERSE_MORSE_CODE_DICT.get(letter_code, "?")
        decoded_text += " "
    return decoded_text.strip()

def main():
    while True:
        try:
            choice = input("\n(D) decrypt, (E) encrypt, (Q) quit: ").strip().upper()

            if choice == "E":
                user_text = input("Enter your text: ").strip()
                if not user_text:
                    print("Please enter something!")
                    continue
                morse_output = encrypt(user_text)
                print("Morse Code:", morse_output)
                continue

            elif choice == "D":
                user_morse_code = input("Enter your Morse Code: ").strip()
                if not user_morse_code:
                    print("Please enter something!")
                    continue
                text_output = decrypt(user_morse_code)
                print("Decoded :", text_output)

            elif choice == "Q":
                print("Bye!")
                break

            else:
                print("Invalid choice. Please select E, D, or Q.")

        except Exception as e:
            print("Oops! Something went wrong:", e)
            print("Let's try again.\n")

if __name__ == "__main__":
    main()