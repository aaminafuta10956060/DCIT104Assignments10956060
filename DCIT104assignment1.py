given_number = int(input("What number would you like to check? "))
numbers_to_check = given_number-1

if given_number <= 2:
    print(f"There are no prime numbers less than {given_number}.")
else:
    is_prime = ""
    list_of_prime = []
    while 1 < numbers_to_check:
        z = 2
        if numbers_to_check == 2:
            is_prime = True
        else:
            while z < numbers_to_check:
                y = numbers_to_check % z
                if y == 0:
                    is_prime = False
                    break
                else:
                    z += 1
                    if numbers_to_check == 3:
                        is_prime = True
                if z == numbers_to_check - 1:
                    is_prime = True
        if is_prime is True:
            list_of_prime.append(numbers_to_check)
        numbers_to_check -= 1

    result = sum(list_of_prime)/len(list_of_prime)

    print(f"The average of all prime numbers less than {given_number} is {result}.")
