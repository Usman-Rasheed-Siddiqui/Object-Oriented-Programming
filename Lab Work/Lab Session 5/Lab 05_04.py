
class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Doctor(Hospital):
    def __init__(self, name, address, specialization):
        super().__init__(name, address)
        self.specialization = specialization

    def print_doctor_name(self):
        print("Doctor Name:", self.name)

class Patient(Hospital):
    def __init__(self, name, address, disease):
        super().__init__(name, address)
        self.disease = disease

    def print_patient_name(self):
        print("Patient Name:", self.name)

class Medical_Test():

    def print_medical_test_info(self, patient, doctor):
        print("Medical Test Info")
        doctor.print_doctor_name()
        patient.print_patient_name()
        print('Disease Diagnosed:', patient.disease)

M1 = Medical_Test()
doctor = Doctor("Mike", "House 2", "MBBS Doctor")
patient = Patient("John", "House 1", "Cholera")
M1.print_medical_test_info(patient, doctor)