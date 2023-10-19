from user_manager import create_user, check_credentials
from file_handler import write_data, read_data

loggedIn = False
userName, password, userType = None, None, None

print("\n*** Welcome to the Medical Data Management System! ***")
print("Sign Up to create user profile. Log In to read or write data.")
input("Press ENTER to continue...")

while not loggedIn:
    print("\nPossible Actions:    1 - Sign Up  |  2 - Log In  |  99 - Quit Program")

    choice = input(">> Enter Your Choice (1 / 2 / 99): ")

    if choice == "99":
        print("\nProgram Terminated.")
        break

    elif choice == "1":
        userName = input(">> Enter Username: ")
        password = input(">> Enter Password: ")
        userType = input(">> Enter User Type (doctor / nurse / lab_technician / patient): ")
        while userType not in ["doctor", "nurse", "lab_technician", "patient"]:
            print("\nThe 'User Type' you entered is invalid.")
            userType = input(">> Enter User Type (doctor / nurse / lab_technician / patient): ")
        else:
            create_user(userName, password, userType)

    elif choice == "2":
        userName = input(">> Enter Username: ")
        password = input(">> Enter Password: ")
        userType, privilegeLevel = check_credentials(userName, password)
        if userType:
            print(f"\nLogin successful! User Type: '{userType}', Privilege Level: {privilegeLevel}")
            loggedIn = True
        else:
            print("\nThe Username or Password you entered is incorrect. Please try again...")

    else:
        print("\nInput is invalid. Please try again...")

while loggedIn:

    if userType in ["doctor", "nurse", "lab_technician"]:
        print("\nPossible Actions:    1 - Read Record  |  2 - Write Record  |  99 - Quit Program")
        choice = input(">> Enter your choice (1 / 2 / 99): ")
        if choice not in ["1", "2", "99"]:
            print("Input is invalid. Please try again...")
            continue
    else: # for 'patients'
        print("\nPossible Actions:    1 - Read record  |  99 - Quit Program")
        choice = input(">> Enter your choice (1 / 99): ")
        if choice not in ["1", "99"]:
            print("\nInput is invalid. Please try again...")
            continue

    if choice == "99":
        print("\nProgram Terminated.")
        break

    if choice == "1":
        print("\nTypes of records available to read:\n\t1 - Personal Details\n\t2 - Sickness Details"
              "\n\t3 - Drug Prescriptions\n\t4 - Lab Test Prescriptions\n")
        typeChoice = input(">> Enter your choice (1 / 2 / 3 / 4): ")
        print()

        dataType = "personal"

        if typeChoice == "1":
            dataType = "personal"
        elif typeChoice == "2":
            dataType = "sickness"
        elif typeChoice == "3":
            dataType = "drug"
        elif typeChoice == "4":
            dataType = "lab"
        else:
            print("Input is invalid. Please try again...")
            continue

        read_data(userName, password, dataType)

    if choice == "2":
        patient = input("\nEnter patient name: ")
        dataType = input("Enter data type (personal, sickness, drug, lab): ")
        data = input("Enter data: ")
        sensitivityLevel = int(input("Enter sensitivity level (0 / 1 / 2 / 3 / 4): "))

        write_data(userName, password, dataType, data, sensitivityLevel, patient)

