from aoc import get_input


# 1
total = 0
for line in get_input(day=1):
    digits = [char for char in line if char.isdigit()]
    total += int(digits[0] + digits[-1])
print(total)

# 2
written_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
def find_digits(line):
    original_line = line
    p = 0
    did_replace = False
    while p < len(line) and not did_replace:
        for letters, digit in written_digits.items():
            if line[p:p+len(letters)] == letters:
                line = line[:p] + str(digit) + line[p+len(letters):]
                did_replace = True
                break
        p += 1
    first_digit = [char for char in line if char.isdigit()][0]

    line = original_line
    p = len(line)
    did_replace = False
    while p >= 0 and not did_replace:
        for letters, digit in written_digits.items():
            if line[p-len(letters):p] == letters:
                line = line[:p-len(letters)] + str(digit) + line[p:]
                did_replace = True
                break
        p -= 1
    last_digit = [char for char in line if char.isdigit()][-1]

    return int(first_digit + last_digit)


total = 0
for line in get_input(day=1):
    total += find_digits(line)

    # # line = 'dljxl7five6nrzfh5one'
    # digits = [char for char in replace_written_digits(line) if char.isdigit()]
    # print(int(digits[0] + digits[-1]), digits, line)
    # total += int(first_digit + digits[-1])
print(total)