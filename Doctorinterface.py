import pandas as pd

data_doctor = pd.read_csv("Doctor.csv")

class Doctor:
    def __init__(self, id, index):
        self.id = id
        self.index = index
        self.name = data_doctor.at[index, "Name"]
        self.specialization = data_doctor.at[index, "Specialization"]

    def info(self):
        doctor_appointment = self.appointment()
        info = [self.id, self.name, self.specialization, doctor_appointment]
        return info

    def appointment(self):
        list_appointment = [
            data_doctor.at[self.index, "Appointment1"],
            data_doctor.at[self.index, "Appointment2"],
            data_doctor.at[self.index, "Appointment3"],
            data_doctor.at[self.index, "Appointment4"],
            data_doctor.at[self.index, "Appointment5"],
            data_doctor.at[self.index, "Appointment6"],
            data_doctor.at[self.index, "Appointment7"]
        ]
        return list_appointment

    def display(self):
        info = self.info()
        print(f"ID: {info[0]}")
        print(f"Name: {info[1]}")
        print(f"Specialization: {info[2]}")
        print(f"Appointments: {info[3]}")

    def Edit_Personal_info(self):
        update_info = ["Name", "Specialization"]
        updates = {}

        for field in update_info:
            updates[field] = input(f"Enter the new {field}:\t ")

        for field in update_info:
            data_doctor.loc[self.index, field] = updates[field]
        data_doctor.to_csv("Doctor.csv", index=False)
        print(f"{self.id} updated successfully.")

    def Edit_Appointment(self):
        update_info = ["Appointment1", "Appointment2", "Appointment3", "Appointment4", "Appointment5", "Appointment6", "Appointment7"]
        updates = {}

        for field in update_info:
            updates[field] = input(f"Enter the Status of {field} :\t").upper()

        for field in update_info:
            data_doctor.loc[self.index, field] = updates[field]

        data_doctor.to_csv("Doctor.csv", index=False)
        print(f"{self.id} updated successfully.")

# Example usage:
# doctor = Doctor(1, 0)
# doctor.display()
# doctor.Edit_Personal_info()
# doctor.Edit_Appointment()
