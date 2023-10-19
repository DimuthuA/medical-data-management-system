import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def create_user(user_name, password, user_type):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == user_name:
                print("Username already exists.")
                return

    privilege_level = 0

    if user_type == "doctor":
        privilege_level = 4
    elif user_type == "nurse":
        privilege_level = 3
    elif user_type == "lab_technician":
        privilege_level = 2
    elif user_type == "patient":
        privilege_level = 1

    hashed_password = hash_password(password)

    with open("users.txt", "a") as user_file:
        user_file.write(f"{user_name},{hashed_password},{user_type},{privilege_level}\n")
        print("Signup successful!")

def check_credentials(user_name, password):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == user_name and data[1] == hash_password(password):
                return data[2], int(data[3])
    return None, 0

def check_user(patient):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == patient and data[2] == "patient":
                return True
    return False
