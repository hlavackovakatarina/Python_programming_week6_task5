def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    analyseValues(values)
    print("Program ending.")

def readValues(filename):
    values = ""
    with open(filename, 'r') as file:
        for line in file:
            values += line.strip() + ";"
    return values

def analyseValues(values):
    print("#### Number analysis - START ####")
    count = countNumbers(values)
    sumNumber = sumNumbers(values)
    greatest = greatestNumber(values)
    average_Number = averageNumber(values)
    print("Count;Sum;Greatest;Average")
    print(f"{count};{sumNumber};{greatest};{average_Number:.2f}")
    print("\n#### Number analysis - END ####")

def countNumbers(values):
    count = 0
    numbers = values.split(";")
    for number in numbers:
        if number != "":
            count += 1
    return count   

def sumNumbers(values):
    sumNumber = 0
    numbers = values.split(";")
    for number in numbers:
        if number != "":
            sumNumber += int(number)
    return sumNumber 

def greatestNumber(values):
    numbers = values.split(";")
    greatest = 1
    for number in numbers:
        if number != "":
            number = int(number)

            if greatest < number:
                greatest = number

    return greatest

def averageNumber(values):
    total = sumNumbers(values)
    count = countNumbers(values)
    average_Number = total / count
    return average_Number

if __name__ == "__main__": #makes sure main runs only when the script is executed directly
    main()