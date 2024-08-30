import sys

english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",
    ".": "..OO.O", ",": "..O...", "?": "..O.O.", "!": "..OOO.", ":": "OO....",
    ";": "..0.0.", "-": "..O..O", "/": ".O..O.", "(": ".O.O.O", ")": ".O.O.O",
    "capital": ".....O", "number": ".O.OOO", "decimal": ".O...O"
}

braille_to_english = {v: k for k, v in english_to_braille.items()}

number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

braille_to_number = {v: k for k, v in number_to_braille.items()}


def is_braille(input_str):
    return all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0


def braille_to_text(braille_str):
    if len(braille_str) % 6 != 0:
        print("Invalid Braille input: length should be a multiple of 6.")
        return ""

    cells = [braille_str[i:i + 6] for i in range(0, len(braille_str), 6)]

    text = []
    capital_next = False
    number_mode = False

    for cell in cells:
        if cell == ".....O":  # Capital follows
            capital_next = True
        elif cell == ".O.OOO":  # Number follows
            number_mode = True
        elif cell == ".O...O":  # Decimal point in number mode
            text.append(".")
        elif cell == "......":  # Space
            text.append(" ")
            number_mode = False  # End number mode on space
        else:
            if number_mode:
                char = braille_to_number.get(cell, "")
            else:
                char = braille_to_english.get(cell, "")
                if capital_next:
                    char = char.upper()
                    capital_next = False

            text.append(char)
            number_mode = False  # Reset number mode after processing the digit

    return "".join(text)


def text_to_braille(text):
    braille = []
    for char in text:
        if char.isupper():
            braille.append(english_to_braille["capital"])
            braille.append(english_to_braille[char.lower()])
        elif char.isdigit():
            if not braille or braille[-1] != english_to_braille["number"]:
                braille.append(english_to_braille["number"])
            braille.append(number_to_braille[char])
        elif char == ".":
            braille.append(english_to_braille["decimal"])
        else:
            braille.append(english_to_braille.get(char, "......"))  # Default to space if char not found
    return "".join(braille)


def main(input_str):
    if is_braille(input_str):
        return braille_to_text(input_str)
    else:
        return text_to_braille(input_str)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
        output_str = main(input_str)
        print(output_str)
    else:
        print("Please provide a string as a command-line argument.")
