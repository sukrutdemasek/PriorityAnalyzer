def analyze_validity():
    while True:
        try:
            devices = float(input("Enter the number of devices: "))

        except ValueError:
            print("Invalid input. Please enter a valid number of devices.")
            continue
        if devices < 0:
            print("The number of devices cannot be negative. Please enter a valid number.")
            continue
        if devices.is_integer() == False:
            print("Please enter a whole number of devices.")
            continue
        return int(devices)

        
            

def analyze_priority(devices):
    if devices == 0:
        problem_priority = "None"
    elif devices == 1:
        problem_priority = "Low"
    elif devices in range(2, 5):
        problem_priority = "Medium"
    elif devices >= 5:
        problem_priority = "High"

    return problem_priority

def print_priority(devices, problem_priority):
    if problem_priority == "None":
        print("There are no devices to analyze.")
    else:    
        print("Number of devices: " + str(devices))
        print("Problem priority: " + problem_priority)
    

def main():
    devices = analyze_validity()
    problem_priority = analyze_priority(devices)
    print_priority(devices, problem_priority)

if __name__ == "__main__":
    main()
