# Non importa pygame
def apply_answer(score: int, is_correct: bool, multiplier: int) -> int:
    try:
        if is_correct:
            score += (10 * multiplier)
            return score
        else:
            score = max(0, score - 5)
            return score

    except (TypeError, ValueError) as e:
        print(f"An error has occured: {e}")
