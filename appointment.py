import pandas as pd
data_Doctor = pd.read_csv('Doctor.csv')
data_patient = pd.read_csv('patient.csv')
specializations = set(data_Doctor['Specialization'])

def choose_specialist():
  print(f"Below specializations are availabel \n {specializations} \n **Choose one from above** \n")
  entered_specialization = input("Enter the specialization of doctor which you need: ")
  
  if entered_specialization in specializations:
    filtered_data = data_Doctor[data_Doctor['Specialization'] == entered_specialization]
    show = filtered_data[['Id','Name','Specialization']]
    print(show)

  else:
    print("Please enter valid specialization")
    return choose_specialist()
  

def choose_Doctor():
      doctor_id = int(input("Enter the doctor id: "))
      if doctor_id in data_Doctor['Id'].values:
            doctor_info = data_Doctor[data_Doctor['Id'] == doctor_id]
            show_slots = doctor_info[[ 'Appointment1', 'Appointment2', 'Appointment3', 'Appointment4', 'Appointment5', 'Appointment6','Appointment7']] 
            print(show_slots)
            return doctor_id
      else:
          print("Enter Id is invalid\n Please Try again By Entering Correct Id")

def get_appointment(appointments,patient_imfo):
    obj = {
        1: "9 am to 10 am",
        2: "10 am to 11 am",
        3: "11 am to 12 pm",
        4: "12 pm to 1 pm",
        5: "2 pm to 3 pm",
        6: "3 pm to 4 pm",
        7: "4 pm to 5 pm"
    }
    for i in range(1, 8):
        if appointments[i - 1] == "SLOT AVAILABLE":
            
            print(f"{i}\t:\t{obj[i]}")
        else:
            print(f"{i}\t:\tAppointment Alredy Fixed ")
    
    Appointment = int(input("Choose the Slot According To Your Need: "))
    if 1 <= Appointment <= 7:
        if appointments[Appointment - 1] == "SLOT AVAILABLE":
            App_msg = f"Appointment Fix \t slot : {obj[Appointment]} \t BY Patient: {patient_imfo[0]} \t Disease : {patient_imfo[1]} "
            appointments[Appointment - 1] = App_msg
            print(f"Appointment Fix  for {obj[Appointment]} This Slot ")
            return appointments
        else:
            print(appointments[Appointment - 1])
    else:
        print("Invalid slot selected.")

def Appointment_alotment(Doctor_id,Patient_id):
    index = data_Doctor.index[data_Doctor['Id'] == Doctor_id].tolist()[0]
    Patient_index = data_patient.index[data_patient['Id'] == Patient_id].tolist()[0]

    appointments = [
        data_Doctor.at[index, 'Appointment1'], 
        data_Doctor.at[index, 'Appointment2'], 
        data_Doctor.at[index, 'Appointment3'], 
        data_Doctor.at[index, 'Appointment4'], 
        data_Doctor.at[index, 'Appointment5'], 
        data_Doctor.at[index, 'Appointment6'], 
        data_Doctor.at[index, 'Appointment7']
    ]
    patient_imfo = [
        data_patient.at[Patient_index,'Name'],
        data_patient.at[Patient_index,'Disease']
    ]

    new_appointments = get_appointment(appointments,patient_imfo)


    data_Doctor.loc[index, 'Appointment1'] = new_appointments[0]
    data_Doctor.loc[index, 'Appointment2'] = new_appointments[1]
    data_Doctor.loc[index, 'Appointment3'] = new_appointments[2]
    data_Doctor.loc[index, 'Appointment4'] = new_appointments[3]
    data_Doctor.loc[index, 'Appointment5'] = new_appointments[4]
    data_Doctor.loc[index, 'Appointment6'] = new_appointments[5]
    data_Doctor.loc[index, 'Appointment7'] = new_appointments[6]
    data_Doctor.to_csv("Doctor.csv", index=False)







      
