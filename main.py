class clsUser:
    def __init__(self, iuserid, iemail,iname,ipassword):
        self.userid = iuserid
        self.email = iemail
        self.name = iname
        self.password = ipassword                

    def changepass(self,newwpass):
        self.password = newwpass
    
    def ChangeEmail(self, newEmail):
        self.email=newEmail
newuser = clsUser(1,"f@g.com","ali",'1234321')
print(f"user's name is {newuser.password}")