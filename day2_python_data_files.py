"""
Day 2 - Python for Data + File Handling

"""

# -----------------------------------------
# EXERCISE 1 - List Comprehension
# -----------------------------------------
print("\n === EXERCISE 1 ===")

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [x for x in numbers if x % 2 == 0]

print("LIST COMPREHENSION:", even_numbers)


# -----------------------------------------
# EXERCISE 2 - Dictionary Comprehension
# -----------------------------------------
print("\n === EXERCISE 2 ===")

squares = {x: x*x for x in range(1,6)}

print("DICTIONARY COMPREHENSION:", squares)


# -----------------------------------------
# EXERCISE 3 - Lambda Function
# -----------------------------------------
print("\n === EXERCISE 3 ===")

data = [('a',5),('b',2),('c',6),('d',8)]

sorted_value = sorted(data, key=lambda x: x[1])

print("SORTED VALUES:", sorted_value)


# -----------------------------------------
# EXERCISE 4 - map()
# -----------------------------------------
print("\n === EXERCISE 4 ===")

words = ["watermelon","lemon","cherry","berry"]

upper_words = list(map(str.upper, words))

print("UPPER WORDS:", upper_words)


# -----------------------------------------
# EXERCISE 5 - filter()
# -----------------------------------------
print("\n === EXERCISE 5 ===")

words = ["dog","giraffe","crocodile","elephant"]

long_words = list(filter(lambda x: len(x) > 4, words))

print("USING FILTER:", long_words)


# -----------------------------------------
# EXERCISE 6 - Read TXT File
# -----------------------------------------
print("\n === EXERCISE 6 ===")

try:
    with open("cleaned.csv","r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)

    print("Lines:", line_count)
    print("Words:", word_count)

except FileNotFoundError:
    print("cleaned.csv file not found")


# -----------------------------------------
# EXERCISE 7 - Error Handling
# -----------------------------------------
print("\n === EXERCISE 7 ===")

try:
    num = int(input("Enter Number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Program Finished")


# -----------------------------------------
# MAIN TASK - CSV Cleaning
# -----------------------------------------
print("\n === MAIN TASK - CSV CLEANING ===")

try:
    input_file = open("messy.csv", "r")
    output_file = open("cleaned.csv", "w")

    for line in input_file:
        columns = [item.strip().lower() for item in line.split(",")]

        # Remove rows with empty values
        if "" not in columns:
            output_file.write(",".join(columns) + "\n")

    input_file.close()
    output_file.close()

    print("CSV Cleaned Successfully")

except FileNotFoundError:
    print("messy.csv file not found")


# -----------------------------------------
# EXERCISE 8 - Read CSV and Filter
# -----------------------------------------

print("\n === EXERCISE 8 ===")

import csv

try:
    with open("cleaned.csv","r") as file:
        reader = csv.reader(file)

        next(reader)  # skip header

        for row in reader:
            if int(row[1]) > 25:
                print(row)

except FileNotFoundError:
    print("cleaned.csv file not found")

# -----------------------------------------
OUTPUT :
# -----------------------------------------

=== EXERCISE 1 ===
LIST COMPREHENSION: [2, 4, 6, 8, 10]

 === EXERCISE 2 ===
DICTIONARY COMPREHENSION: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

 === EXERCISE 3 ===
SORTED VALUES: [('b', 2), ('a', 5), ('c', 6), ('d', 8)]

 === EXERCISE 4 ===
UPPER WORDS: ['WATERMELON', 'LEMON', 'CHERRY', 'BERRY']

 === EXERCISE 5 ===
USING FILTER: ['giraffe', 'crocodile', 'elephant']

 === EXERCISE 6 ===
Lines: 4
Words: 4

 === EXERCISE 7 ===
Enter Number: 200
0.5
Program Finished

 === MAIN TASK - CSV CLEANING ===
CSV Cleaned Successfully

 === EXERCISE 8 ===
['eve', '28', 'bangalore', '70000']
['frank', '33', 'pune', '55000']
