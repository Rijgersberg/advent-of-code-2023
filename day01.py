from aoc import get_input

written_digits = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def first_digit(line, use_letters=False):
    for p in range(len(line)):
        if line[p].isdigit():
            return line[p]
        elif use_letters:
            for letters, digit in written_digits.items():
                if line[p:p+len(letters)] == letters:
                    return digit

def last_digit(line, use_letters=False):
    for p in range(len(line)-1, -1, -1):
        if line[p].isdigit():
            return line[p]
        elif use_letters:
            for letters, digit in written_digits.items():
                if line[p-len(letters)+1:p+1] == letters:
                    return digit

# 1
print(sum(int(first_digit(line) + last_digit(line)) for line in get_input(day=1)))

#2
print(sum(int(first_digit(line, use_letters=True) + last_digit(line, use_letters=True))
          for line in get_input(day=1)))
