# Create a python program to implement Morse Code Translator.
morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

choice = input("1. English to Morse Code\n2. Morse Code to English\nEnter your choice: ")

if choice == '1':
    text = input("Enter English text: ").upper()
    result = ""

    for char in text:
        if char == ' ':
            result += "/ "
        elif char in morse_code:
            result += morse_code[char] + " "

    print("Morse Code:", result)

elif choice == '2':
    code = input("Enter Morse Code (separate letters with spaces and words with /): ")
    words = code.split(" / ")
    result = ""

    for word in words:
        letters = word.split()

        for letter in letters:
            for key, value in morse_code.items():
                if value == letter:
                    result += key

        result += " "

    print("English Text:", result.strip())

else:
    print("Invalid choice!")