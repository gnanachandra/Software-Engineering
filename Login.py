class Login:

    def __init__(self,emailid,password):
        self.emailid=emailid
        self.password=password
    def verifyDetails(self):
        #opening emailsfile  and storing the emails in the form of list 
        e=open("emailsfile.txt","r")
        edetails=e.read()
        emaillist=edetails.split("\n")
        #opening passwords file and storing them in the form of list
        p=open("passwordsfile.txt","r")
        pdetails=p.read()
        passwordslist=pdetails.split("\n")
        for email in emaillist:
            if(self.emailid==email):
                if(self.password==passwordslist[emaillist.index(email)]):
                    return 1
                return 0
        return -1
#end of class Login 

useremail=input("enter emailID:")

str="@vvit.net"
if str not in useremail:
    while(str not in useremail):
        print("enter a valid email(use organisation mail:):")
        useremail=input()

password=input("enter password:")
while(len(password)<5):
    print("entered password is less than 5 characters ")
    print("enter correct password")
    password=input("enter password:")


object=Login(useremail,password)
response=object.verifyDetails()
if(response==1):
    print("login successful ")
elif(response==0):
    print("entered password is incorrect")
else:
    print("user not registered please click on register")