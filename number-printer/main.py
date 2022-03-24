# Write a program in Python or Java that counts backwards from 100 to 1 and prints:
# “Agile” if the number is divisible by 5,
# “Software” if the number is divisible by 3,
# “Testing” if the number is divisible by both,
# or prints just the number if none of those cases are true.

def number_printer():
    for number in range(100, 0, -1):
        if number % 5 == 0 and number % 3 == 0:
            print("Testing")

        elif number % 3 == 0:
            print("Software")

        elif number % 5 == 0:
            print("Agile")

        else:
            print(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number_printer()
