"""
This script calculates the sum of all odd numbers from 1 to 100 and counts
the occurrences of the first letter in a provided name.
"""

# Constants
START = 1
END = 101
STEP = 2
NAME_PROMPT = 'Введіть ім\'я: '
SUM_MESSAGE = 'Сума всіх непарних чисел від 1 до 100:'
LETTER_COUNT_MESSAGE = 'Кількість входжень першої букви:'
EMPTY_NAME_MESSAGE = 'Ім\'я не може бути порожнім.'

# Calculation of the sum of all odd numbers from 1 to 100
TOTAL_SUM = 0

for NUMBER in range(START, END, STEP):
    TOTAL_SUM += NUMBER

print(SUM_MESSAGE, TOTAL_SUM)

# Counting occurrences of the first letter in the provided name
name = input(NAME_PROMPT)

if name:  # Check if the name is not empty
    FIRST_LETTER = name[0]
    LETTER_COUNT = 0
    for LETTER in name:
        if LETTER == FIRST_LETTER:
            LETTER_COUNT += 1

    print(LETTER_COUNT_MESSAGE, LETTER_COUNT)
else:
    print(EMPTY_NAME_MESSAGE)
