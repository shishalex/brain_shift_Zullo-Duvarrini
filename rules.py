# Non importa pygame
def is_even(number: int) -> bool:
    try:
        if number % 2 == 0:
            return True
        else:
            return False
    except (TypeError, ValueError) as e:
        print(f"The character is not a number: {e}")

def is_vowel(letter: str) -> bool:
    try:
        if letter.lower() in 'aeiou':
            return True
        else:
            return False
    except (TypeError, ValueError) as e:
        print(f"The character is not a letter: {e}")


def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    try:
        if position.lower() == "top":
            if is_even(number):
                return True
            else:
                return False
        elif position.lower() == "bottom":
            if is_vowel(letter):
                return True
            else:
                return False
    except (TypeError, ValueError) as e:
        print(f"The character is not valid: {e}")