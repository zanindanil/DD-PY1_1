list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = 0
b = list_numbers[a]

for current_index, current_number in enumerate(list_numbers):
    if current_number > b:
        b = current_number
        a = current_index
list_numbers[a], list_numbers[-1] = list_numbers[-1], list_numbers[a]

print(list_numbers)

