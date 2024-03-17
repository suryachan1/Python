#abstraction  abc=abstract base class import
#before abstract method use '@abstract method' indicate after the method is abstract method
#in abstraction only fn can access the data 
'''ques)create a class ticket which will be the abstract class inside that create a fn bookticket which will be the abstract method and as nothing in it.
        create a class makemytrip which will use the boookticket fn from ticket class to take the details such as name pno email journey date and displays a mess saying thank you for booking from make mytrip.
        create a class irctc which uses the bookticket of ticket class and take this same details as make mytrip but in the end i will give an option to the user to select wheather it is one way or roundtrip
        if the user option round trip it again ask the user to enter the return date as well and then print a mess thankyou for choosing irctc
        else it prints the mess thankyou foor choosing ircts.
        create a class indico which takes alll the details as irctc and just asks which mode of transport you are to go in train flight and bus and this place thankyou choosing for__'''
#class becomes abstract when @abstract method i.e (from abc import ABC,abstractmethod ) used at top
from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class MakeMyTrip(Ticket):
    def book_ticket(self,name,p_no,eid,journey):
        print("Ticket for ",name,"booked successfully.Boarding on",journey)
        print("Thank You for booking from MakeMyTrip")
class IRCTC(Ticket):
    def book_ticket(self,name,p_no,eid,journey):
        end_date=input("Want you want 1.One way trip 2.Round trip")
        if(end_date=="1" or end_date=="One way trip"):
            print("Ticket for ",name,"booked successfully.Boarding on",journey)
            print("Thank You for booking from IRCTC")
        elif(end_date=="2" or end_date=="Round Trip"):
            end=input("Enter the return date:")
            print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
            print("Thank You for booking from IRCTC")
        else:
            print("Invalid")
class Indigo(Ticket):
    def book_ticket(self,name,p_no,eid,journey):
        choice=input("What you want 1.Flight 2.Train 3.Bus")
        if(choice=="1" or choice=="Flight"):
            end_date=input("Want you want 1.One way trip 2.Round trip")
            if(end_date=="1" or end_date=="One way trip"):
                print("Ticket for ",name,"booked successfully.Boarding on",journey)
                print("Thank You for booking from Indigo")
            else:
                end=input("Enter the return date:")
                print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
                print("Thank You for booking from Indigo")
        elif(choice=="2" or choice=="Train"):
            end_date=input("Want you want 1.One way trip 2.Round trip")
            if(end_date=="1" or end_date=="One way trip"):
                print("Ticket for ",name,"booked successfully.Boarding on",journey)
                print("Thank You for booking from Indigo")
            else:
                end=input("Enter the return date:")
                print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
                print("Thank You for booking from Indigo")
        elif(choice=="3" or choice=="Bus"):
            end_date=input("Want you want 1.One way trip 2.Round trip")
            if(end_date=="1" or end_date=="One way trip"):
                print("Ticket for ",name,"booked successfully.Boarding on",journey)
                print("Thank You for booking from Indigo")
            else:
                end=input("Enter the return date:")
                print("Ticket for ",name,"booked successfully.Boarding on",journey,"Return date",end)
                print("Thank You for booking from Indigo")
        else:
            print("Invalid")
inp=input("Enter want you want 1.Make My Trip 2.Irctc 3.Indigo:")
if(inp=="Make My Trip" or inp=="1"):
   obj=MakeMyTrip()
   obj.book_ticket(input("Enter name:"),input("Enter phone:"),input("Enter email:"),input("Enter journey date:"))
elif(inp=="Irctc"or inp=="2"):
    obj1=IRCTC()
    obj1.book_ticket(input("Enter name:"),input("Enter phone:"),input("Enter email:"),input("Enter journey date:"))
elif(inp=="Indigo"or inp=="3"):
    obj2=Indigo()
    obj2.book_ticket(input("Enter name:"),input("Enter phone:"),input("Enter email:"),input("Enter journey date:"))
else:
    print("invalid selection")    
    
