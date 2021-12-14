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

useremail=input("enter emailID:")
password=input("enter password:")
object=Login(useremail,password)
response=object.verifyDetails()
if(response==1):
    print("login successful ")
elif(response==0):
    print("entered password is incorrect")
else:
    print("user not registered please click on register")