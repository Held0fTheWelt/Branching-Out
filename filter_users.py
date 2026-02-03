import json

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    
    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["age"] == age]
    
    for user in filtered_users:
        print(user)

def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('name' 'age' or 'email' is supported): ").strip().lower()

    type_option = ""
    if filter_option == "name":
        type_option = "a name"
    elif filter_option == "email":
        type_option = "an email"
    elif filter_option == "age":
        type_option = "an age"

    search_value  = input(f"Enter {type_option} to filter users: ").strip()

    if filter_option == "name":
        filter_users_by_name(search_value)
    elif filter_option == "email":
        filter_users_by_email(search_value)
    elif filter_option == "age":
        try:
            age = int(search_value)
        except ValueError:
            print("Please enter a valid integer for age.")
        else:
            filter_users_by_age(age)

    else:
        print("Filtering by that option is not yet supported.")