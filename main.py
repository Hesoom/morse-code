# morse code translator
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


def encryption(text):
    #Translate the plain text to morse code
    encypted_text = ""
    #Check if user wrote any text
    if text:
        text = text.upper()
        for letter in text:
            if letter in MORSE_CODE_DICT:
                encypted_text += MORSE_CODE_DICT[letter]
            else:
                encypted_text += "?"

        return encypted_text
    else:
        print("At least write 1 character!")
        main()

def main():
    while True:
        user_input = input("Enter your text: ")
        if not user_input:
            print("Enter something atleast!")
            continue
        morse_output = encryption(user_input)
        print(morse_output)

if __name__ == "__main__":
    main()