import re

file = open('exercise1_input.txt', 'r')

def search_and_replace_digits(raw_string):
  letter_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  numbers = ['o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9n']

  for letter_digit, number in zip(letter_digits, numbers):  
    raw_string = re.sub(letter_digit, number, raw_string)

  return raw_string

def main():
  acc = 0

  for line in file:
    line_parsed = search_and_replace_digits(line)

    line_digits = re.findall(r'\d+', line_parsed)

    result_number = ''.join(line_digits)

    first_digit = result_number[0]
    last_digit = result_number[-1]

    line_number = f"{first_digit}{last_digit}"

    acc += int(line_number)

  print(f"the result is {acc}")

main()

