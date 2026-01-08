from datetime import datetime

def analyze_numbers(numbers):
    # This function takes a list of numbers and returns basic statistics.
    if not numbers:
        return None
    

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    return {
        "total": total,
        "count": count,
        "average": average,
        "min": minimum,
        "max": maximum
    }
 

def collect_and_analyze():
    numbers = []
    count = int(input("How many numbers would you like to enter?: "))
    while True:
        if count > 0:
            break
        try:
            count = int(input("Please enter a positive integer for how many numbers you'd like to enter: "))
            if count <= 0:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("You entered the following numbers:")
    for num in numbers:
        print(num, end=" ")
        print()
    
    results = analyze_numbers(numbers)
    if results:
        print("\nStatistics:")
        print(f"Total: {results.get('total')}")
        print(f"Count: {results.get('count')}")
        print(f"Average: {results.get('average'):.2f}")
        print(f"Minimum: {results.get('min')}")
        print(f"Maximum: {results.get('max')}")
    else:
        print("No numbers to analyze.")
    
    #save results to a file named report.txt
    #include a timestamp of when the analysis was performed
    #overwrite the file if it already exists
    #do not create a new function for this task
    
    with open("report.txt", "w") as f:
        f.write(f"Analysis Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("Numbers Entered:\n")
        for num in numbers:
            f.write(f"{num}\n")
        f.write("\nStatistics:\n")
        f.write(f"Total: {results.get('total')}\n")
        f.write(f"Count: {results.get('count')}\n")
        f.write(f"Average: {results.get('average'):.2f}\n")
        f.write(f"Minimum: {results.get('min')}\n")
        f.write(f"Maximum: {results.get('max')}\n")
    print("\nAnalysis report saved to report.txt")


def main():

    # show menu options
    #1) Enter numbers and analyze
    #2) Exit the program
    # Ask user to choose an option
    while True:
        print("\nMenu:")
        print("1) Enter numbers and analyze")
        print("2) Exit the program")
        choice = input("Please choose an option (1 or 2): ")
        if choice == "1":
            collect_and_analyze()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    


if __name__ == "__main__":
    main()

