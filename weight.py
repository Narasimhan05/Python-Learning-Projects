# Python weight converter

weight = float(input('Enter your weight: '))
unit = input('Enter (L)bs or (K)g: ')

if unit.upper() == 'L':
    weight = weight * 0.45
    unit = 'kilos'
else:
    weight = weight / 0.45
    unit = 'pounds'

print(f'Your weight is {round(weight, 1)} {unit}')