# Importong Library
import pandas as pd
import login as login
import Doctorinterface as Doctor
import patientinterface as Patient
import appointment as Ap

# Checking if user is Doctor or Patient
person = int(input("1.Doctor\n2.Patient\n:\t"))
Exit_c = True
while Exit_c:
    if person == 1: #User is Doctor
        filename = 'Doctor.csv'
        data_doctor = pd.read_csv(filename)
        fields = ["Name", "Specialization","Appointment1","Appointment2","Appointment3","Appointment4","Appointment5","Appointment6","Appointment7"]
        operation = login.LoginCreate(filename,data_doctor,fields)
        id = operation.choices_function()
        index_list = data_doctor.index[data_doctor["Id"] == id].tolist()

        if index_list:
            index = index_list[0]
            doctor = Doctor.Doctor(id, index)
        else:
            print("Doctor ID not found")

        Exit_D = False
        while not Exit_D:
            operation = int(input("1.Display \n2.Edit_Appointment \n3.Edit_Personal_Imfo \n4.Exit\n\t\t:\t"))

            if operation == 1:
                doctor.display()
            elif operation == 2:
                doctor.Edit_Appointment()
            elif operation == 3:
                doctor.Edit_Personal_imfo()
            elif operation == 4:
                print("Thank you for visiting.....!")
                Exit_D = True
            else:
                print("You entered a wrong number. Please try again.")

    elif person == 2:
        filename = 'patient.csv'
        data_patient = pd.read_csv(filename)
        filed = ["Name", "Disease"]
        operation = login.LoginCreate(filename,data_patient,filed)
        patient_id = operation.choices_function()
        index_list = data_patient.index[data_patient["Id"] == patient_id].tolist()

        if index_list:
            index = index_list[0]
            patient_obj = Patient.Patient(patient_id, index)
        else:
            print("Patient ID not found")

        Exit_P = False
        while not Exit_P:
            operation = int(input("1.Display  \n2.Edit Personal Info \n3. Take Appointment 4.Exit\n\t\t:\t"))

            if operation == 1:
                patient_obj.display()
            elif operation == 2:
                patient_obj.Edit_Personal_info()
            elif operation == 3:
                Exit_A = False

                Ap.choose_specialist()
                doctor_id = Ap.choose_Doctor()
                while not Exit_A:
                    status = int(input("Do you want to:\n1. Book an Appointment\n2. Choose Another Doctor\n3. Change Specialization\n4. Exit\n\t\t:"))

                    if status == 1:
                        Ap.Appointment_alotment(doctor_id, patient_id)
                    elif status == 2:
                        doctor_id = Ap.choose_Doctor()
                    elif status == 3:
                        Ap.choose_specialist()
                    elif status == 4:
                        Exit_A = True
                        print("Thank you for visiting!")
                    else:
                        print("Entered choice is invalid. Please try again.")
            elif operation == 4:
                print("Thank you for visiting!")
                Exit_P = True

            else:
                print("Invalid input. Please try again.")
        break
    else:
        print("You have entered a wrong choice. Please try again.")