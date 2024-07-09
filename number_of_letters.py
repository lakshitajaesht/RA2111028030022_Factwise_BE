def num_letters(n):
  
  ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
          6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

  teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
           15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

  tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
          7: 'seventy', 8: 'eighty', 9: 'ninety'}

  one_hundred = 7
  hundred_letters = 3 
  thousand_letters = 11
  total_letters = 0

  if n <= 999:
    hundreds = n // 100
    if hundreds > 0:
      total_letters += one_hundred if hundreds == 1 else hundred_letters * hundreds
      total_letters += 3  # "and"

    remaining = n % 100
    if remaining > 0:
      if remaining <= 19:
        total_letters += len(teens[remaining])
      else:
        tens_digit = remaining // 10
        ones_digit = remaining % 10
        total_letters += len(tens[tens_digit])
        total_letters += len(ones[ones_digit])

  elif n == 1000:
    total_letters = thousand_letters

  return total_letters

total_letters = 0
for i in range(1, 1001):
  total_letters += num_letters(i)

print("Total letters used:", total_letters)
