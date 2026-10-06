class Hospital:
    def __init__(self):
        self.hname=input('Enter the Hospital name:')
        self.location=input('Enter the location')
    def showDetails(self):
        print('Hospital name:',self.hname)
        print('Location:',self.location)
class Department:
    def __init__(self):
        self.departmentName=input('Enter the department name')
        self.docname=input('Enter the doctor name')
    def showdeptdetails(self):
        print('Department Name:',self.departmentName)
        print('Doctor name:',self.docname)
class Patient(Hospital,Department):
    def __init__(self):
        Hospital().__init__()
        Department().__init__()
        self.id=input("Enter the Patient id:")
        self.name=input('Enter the patient name')
        self.gender=input('Enter your gender')
        self.place=input('Enter your place')
        self.admn_date=int(input('Enter the admission date'))
        self.dischargedate=''
    def setdischargedate(self):
        self.dischargedate = input('Enter the date of discharge')
    def fullsummary(self):
        Hospital().__init__()
        Department().__init__()
        print('Patient Name:',self.name)
        print('Id:',self.id)
        print('Gender:',self.gender)
        print('Place:',self.place)
        print('Admission Date:',self.admn_date)
        print('Discharge Date:',self.dischargedate)

        if self.dischargedate=='':
            print('Not yet discharged,')
        else:
            print('Discharged date:',self.dischargedate)

p=Patient()
p.fullsummary()