import pandas as pd
import hashlib as hash

class LoginCreate:
    def __init__(self, filename, data, fields):
        self.filename = filename
        self.data = data
        self.fields = fields

    def choices_function(self):
        choices = int(input("Do You Want to \n 1. Log-in \n 2. Create Account\n"))
        if choices == 1:
            id_to_transfer = self.login()
        elif choices == 2:
            id_to_transfer = self.create()
        else:
            print("You Have Entered Wrong choice")
            id_to_transfer = None
        return id_to_transfer

    def login(self):
        id_ = int(input("Enter Your Id:\t"))
        password = str(input("Enter Your Password:\t"))
        password_hash = hash.sha256(password.encode()).hexdigest()
        index = self.data.index[self.data["Id"] == id_].tolist()
        if index:
            if password_hash == self.data.at[index[0], 'Password']:
                print("Login Successfully")
                return id_
        print("ID Entered is Invalid")
        return self.choices_function()

    def create(self):
        new_entry = {}
        new_id = self.id_generator()
        new_entry["Id"] = new_id
        password_create = str(input("Create A Password: "))
        password_hash_create = hash.sha256(password_create.encode()).hexdigest()
        new_entry["Password"] = password_hash_create
        print(f"Id of This Person Will be {new_entry['Id']}")

        for field in self.fields:
            new_entry[field] = input(f"Enter {field}: ")

        
        # Append new entry to DataFrame using pd.concat
        new_entry_df = pd.DataFrame([new_entry])
        self.data = pd.concat([self.data, new_entry_df], ignore_index=True)
        self.data.to_csv(self.filename, index=False)
        print("New entry added successfully.")
        print("\n\nNow Login To Continue Further...")
        return self.login()

    def id_generator(self):
        num = len(self.data) + 2
        if self.filename == 'Doctor.csv':
            id_ = 61230000 + num
        else:
            id_ = 21300000 + num
        return id_

# Example usage:
# data_doctor = pd.read_csv("Doctor.csv")
# fields = ["Name", "Specialization"]
# login_create = LoginCreate("Doctor.csv", data_doctor, fields)
# login_create.choices_function()
