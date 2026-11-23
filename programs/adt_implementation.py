# Employee Abstract Data Type

class Employee:
    def GetEmployee(self):
        print("Enter Employee Details")
        self.id = input("Id : ")
        self.name = input("Name : ")
        self.sal = int(input("Salary : "))
        return

    def Salary(self):
        da = self.sal * 40 / 100
        hra = self.sal * 16 / 100
        self.ns = self.sal + da + hra
        return

    def Display(self):
        print(" %5s %25s %10s %10s" %(self.id, self.name, self.sal, self.ns))
        return

# Main
n = int(input("Enter Total number of Employee : "))
emplist = []
for i in range(n):
    e = Employee()
    e.GetEmployee()
    e.Salary()
    emplist.append(e)

print ("-----------------------------------------------")
print(" Employee Details")
print("%5s %25s %10s %10s" %("Id", "Name", "Salary", "Net Salary"))
print ("-------------------------------------------------")

for e in emplist:
    e.Display()