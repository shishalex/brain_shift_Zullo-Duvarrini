# Non importa pygame
def apply_answer(score: int, is_correct: bool, multiplier: int) -> int:
    try:
        if is_correct:
            return score + 10 * multiplier
        else:
            return score - 5
    except (TypeError, ValueError) as e:
        print(f"An error occured: {e}")
