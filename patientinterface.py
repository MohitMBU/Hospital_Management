import pandas as pd

data_patient = pd.read_csv("patient.csv")

class Patient:
    def __init__(self, id, index):
        self.id = id
        self.index = index
        self.name = data_patient.at[index, "Name"]
        self.Disease = data_patient.at[index, "Disease"]
    
    def display(self):
        info = [self.id, self.name, self.Disease]
        print(f"ID: {info[0]}")
        print(f"Name: {info[1]}")
        print(f"Disease: {info[2]}")
    
      
    def Edit_Personal_info(self):
        edit_p = int(input("What do you want to change? \n 1.Name - Enter 1 \n 2. Disease - Enter 2  \n 3.Both - Enter 3:\t"))
        if edit_p == 1:
            print(f"Your Current Name is {self.name}.\n")
            new_name = input("\nEnter new Name : ")
            data_patient.loc[self.index, "Name"] = new_name
            data_patient.to_csv("patient.csv", index=False)
        elif edit_p == 2:
            print(f"Your current Disease info: {self.Disease}")
            new_disease = input("Enter new Disease :")
            data_patient.loc[self.index, "Disease"] = new_disease
            data_patient.to_csv("patient.csv", index=False)
        elif edit_p == 3:
            update_info = ["Name", "Disease"]
            for field in update_info:
                data_patient.loc[self.index, field] = input(f"Enter the new {field}:\t ")
            data_patient.to_csv("patient.csv", index=False)
            print(f"{self.id} updated successfully.")
        else:
            print("Invalid input")


