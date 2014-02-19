# This class encapsulates all communication with the DB
from users.models import User
from django.db.models import Q

class UsersModel (object):
    
    SUCCESS = 1
    ERR_BAD_CREDENTIALS = -1
    ERR_USER_EXISTS = -2
    ERR_BAD_USERNAME = -3
    ERR_BAD_PASSWORD = -4
    Err_Num = -1
    Good_Num = 1
    MAX_USERNAME_LENGTH = 128
    MAX_PASSWORD_LENGTH = 128
    
    def __init__(self):
        # do nothing
        pass
        

    def add(self, userName, passWord):
        # we have to check if username or password is None first
        if userName is None:
            return (UsersModel.ERR_BAD_USERNAME, self.Err_Num)
        if passWord is None:
            return (UsersModel.ERR_BAD_PASSWORD, self.Err_Num)
        if len(userName) > UsersModel.MAX_USERNAME_LENGTH or len(userName) == 0 : # check if username is valid
            return (UsersModel.ERR_BAD_USERNAME, self.Err_Num)
        if len(passWord) > UsersModel.MAX_PASSWORD_LENGTH: # check if password is valid
            return (UsersModel.ERR_BAD_PASSWORD, self.Err_Num)

        try:
            newOne = User.objects.get(Q(user = userName)) # username must be unique
            return (UsersModel.ERR_USER_EXISTS, self.Err_Num)
        except:
            newOne = User(userName, passWord)
            newOne.count += 1
            newOne.save()
            return (UsersModel.SUCCESS, newOne.count)



    def login(self, userName, passWord):
        

        if userName is None:
            return (UsersModel.ERR_BAD_USERNAME, self.Err_Num)
        if passWord is None:
            return (UsersModel.ERR_BAD_PASSWORD, self.Err_Num)
        if len(userName) > UsersModel.MAX_USERNAME_LENGTH or len(userName) == 0 : 
            return (UsersModel.ERR_BAD_USERNAME, self.Err_Num)
        if len(passWord) > UsersModel.MAX_PASSWORD_LENGTH: 
            return (UsersModel.ERR_BAD_PASSWORD, self.Err_Num)
        try:
            userInfo = User.objects.get(Q(user = userName), Q(password = passWord))
            userInfo.count += 1
            userInfo.save()
            return (UsersModel.SUCCESS, userInfo.count)
        except:
            return (UsersModel.ERR_BAD_CREDENTIALS, self.Err_Num)

        
    def TESTAPI_resetFixture(self):
        User.objects.all().delete()
        return UsersModel.SUCCESS
