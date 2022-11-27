class Company:
    def __init__(self,iname):
        self.iname=iname ##Class Instance Name
        self.companyName = input("Enter Company Name: ")
        self.executeQ=True

    def program(self,): ## if booms :)
        select = self.menu()
        if select == "1":
            self.addStaff()
        if select == "2":
            self.discardStaff()
        if select == "3":
            m_a_type=input("Wage Type MONTH or YEAR ?(M/Y): ")
            if m_a_type == 'M': 
                self.showWage(aType="M")
            elif m_a_type == 'Y':
                self.showWage(aType="Y")
            else:
                print("ERROR VALUES Program closing.")
                exit()
        if select == "4":
            self.exit_()


    
    def menu(self):
        select = input(f"***** WELCOME TO {self.companyName},{self.iname} OOP PROGRAM ******\n\n1- Add Staff\n2- Discard Staff\n3- Show Wage\n4- Exit\n Please write it here: ")
        return select
            
 

    def addStaff(self):

        with open("Staff.txt","r",encoding="UTF-8") as file:
            staffList = file.read()
        print(staffList)

        id= 1
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        wage = input("Enter wage: ")


        if len(staffList) == 0:
            id = 1
        else:
            with open("Staff.txt","r",encoding="UTF-8") as file:
                id = int(file.readlines()[-1].split(")")[0]) + 1

    
        with open("Staff.txt","a+",encoding="UTF-8") as file:
            file.write(f"{id}){name}-{surname}-{age}-{gender}-{wage}\n")




    def discardStaff(self):
        with open("Staff.txt","r",encoding="UTF-8")  as file:
            staffs = file.readlines()


        cList = []
        for staff in staffs:
            cList.append(staff[:-1].replace("-"," "))

        for staff2 in cList:
            print(staff2)

        print("***********************")
        print("***********************")
        print("***********************")

        select = int(input("ID to be DELETED: "))
        cList.pop(select-1)


        yList= []
        counterX = 1
        for staff3 in cList:
            yList.append(str(counterX) + staff3[1:])
            counterX += 1

        for staff4 in yList:
            print(staff4)

        with open("Staff.txt","w",encoding="UTF-8") as file:
            for x in yList:
                file.write(x)
                file.write("\n")



    def showWage(self,aType="m"):
        # Account Type Info:   Mounth=m  Year=y
        with open("Staff.txt","r",encoding="UTF-8") as file:
            staffList = file.readlines()

        wagesList = []    
        for staff in staffList:
            wagesList.append(int(staff.split("-")[-1]))
        
        if aType =='M':
            print(f"Wage per Mounth:{sum(wagesList)}")
        elif aType =='Y':
            print(f"Wage per Mounth:{sum(wagesList)*12}")
        else: 
            errshowWage = ("ERROR showWage\n")*5
            print(errshowWage)
            print("The program is closing")
            exit()
            

    def exit_(self):
        exit()



s1 = Company("Instance NAME")
#while s1.executeQ:
while True:
    s1.program()