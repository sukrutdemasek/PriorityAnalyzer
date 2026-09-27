def analyze_validity():
    try:
        devices = float(input("Enter the number of devices: "))
    except ValueError:
        print("Invalid input. Please enter a valid number of devices.")
        return analyze_validity()
    
    if devices.is_integer() == False:
        print("Please enter a whole number of devices.")
        return analyze_validity()

    else:
        return devices

def analyze_priority(devices):
    problem_priority_list = ["High", "Medium", "Low", "None"]
    
    if devices < 0:
        print("Invalid input. Please enter a valid number of devices.")

    elif devices == 0:
        print ("The problem is not confirmed.")
        problem_priority = problem_priority_list[3]

    elif devices == 1:
        print("Priority: " + problem_priority_list[2])
        problem_priority = problem_priority_list[2]
    elif devices in range(2, 4):
        print("Priority: " + problem_priority_list[1])
        problem_priority = problem_priority_list[1]
    elif devices >= 4:
        print("Priority: " + problem_priority_list[0])
        problem_priority = problem_priority_list[0]
    else:
        print("Invalid input. Please enter a valid number of devices.")
        return analyze_priority(devices)  # Recursively call the function for valid input


def main():
    devices = analyze_validity()
    analyze_priority(devices)

if __name__ == "__main__":
    main()
