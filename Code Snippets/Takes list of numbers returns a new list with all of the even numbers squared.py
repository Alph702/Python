def square_evens(num : list[int]):
    square_evens = []
    for number in num:
        if number % 2 == 0:
            square_evens.append(number**2)
    return square_evens


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(square_evens(numbers))