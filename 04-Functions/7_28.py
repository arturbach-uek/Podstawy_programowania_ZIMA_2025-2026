def number_with_longest_streak(dice):
    max_streak = 1
    current_streak = 1
    number_with_streak = dice[0]

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            number_with_streak = dice
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
                number_with_streak = dice[i]
            else:
                current_streak = 1

    return number_with_streak

print(_("2133"))