def verifyemail(email):
        str="@vvit.net"
        while(str not in email):
            print("enter organisation mail(vvit.net mail)")
            email=input()
        return email

class Register:

    def checkdata(self,email,password):
        e=open("emailsfile.txt","r")
        edetails=e.read()
        emaillist=edetails.split("\n")
        p=open("passwordsfile.txt","w")
        pdetails=p.read()
        passwordslist=pdetails.split("\n")
        if email not in emaillist:
            
            e.write(email)
        
            p.write(password)
            return 1
        return 0
    
    def addDetails(self,name,rollno,branch):
        dfile=open("datafile.txt","w")
        dfile.write("name:{} rollnumber:{} branch:{} ".format(name,rollno,branch))
        dfile.write("\n")


name=input("enter name:")
rollno=input("enter student roll number")
branch=input("enter branch and section ")
email=input("enter email")
email=verifyemail(email)
password=input("create a new password (more than 5 characters:")
while(len(password)<=5):
    print("the password is less than 5 characters")
    print("reenter password:")
    password=input()
cpassword=input("confirm your password:")
while(password!=cpassword):
    print("entered passwords donot match")
    print("confirm your password again")
    cpassword=input()

obj=Register()
response=obj.checkdata(email,password)
if(response==1):
    obj.adddetails(name,rollno,branch)
    print("user is registered successfully")
    print("continue to login HAPPY LEARNING")
elif(response==0):
    print("user already registered")

