from collections import Counter
import random

from constants import MULTIPLIERS


def gamble_karma(amount=1):
    multiplier_keys = list(MULTIPLIERS.keys())

    slots = [random.choice(multiplier_keys) for _ in range(0, 3)]

    slot, count = max(Counter(slots).items(), key=lambda count: count[1])

    amount_to_win = 0
    if count == 2:
        amount_to_win = int(amount * MULTIPLIERS[slot] * .2)
    if count == 3:
        amount_to_win = amount * MULTIPLIERS[slot]

    return amount_to_win
