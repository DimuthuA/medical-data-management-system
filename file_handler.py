import time
from user_manager import check_credentials, check_user

def read_data(username, password, data_type):
    user_type, privilege_level = check_credentials(username, password)
    found_data = False 

    try:
        with open("data.txt", "r") as data_file:
            for line in data_file:
                if line != "":
                    data = line.strip().split(",")
                    sensitivity_level = int(data[3])

                    if (((user_type == "patient" and data[0] == username) or
                        user_type in ["doctor", "nurse", "lab_technician"]) and
                        data[1] == data_type and privilege_level >= sensitivity_level):

                        print(f"-- Patient: {data[0]} | Data: {data[2]} | Date:{data[4]} ")
                        found_data = True

        if not found_data:
            print("\nNot found! No entries for the type you requested.")

    except FileNotFoundError:
        print("\nError! File containing the data is not found.")
        
    except Exception as e:
        print(f"\nError! An error occurred: {str(e)}")


def write_data(username, password, data_type, data, sensitivity_level, patient):
    privilege_level = check_credentials(username, password)[1]

    if privilege_level < sensitivity_level:
        print("Sorry! You don't have the required privilege level to write this record.")
        return
    if not check_user(patient):
        print("Error! The patient you entered does not exist.")
        return

    current_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

    with open("data.txt", "a") as data_file:
        data_file.write(f"{patient},{data_type},{data},{sensitivity_level},{formatted_time}\n")
        print("Data written successfully.")
