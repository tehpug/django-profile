from django.contrib.auth.models import User

class UserManager(object):
    def addNewUser(self,**kwargs):
        '''
        >>>addNewUser(username='nima',email='nim4n@yahoo.com',password='nima')
        >>>
        '''
        userObj = User.objects.create_user(username=kwargs['username'],email=kwargs['email'],password=kwargs['password'])
        return obj
    def createSuperUser(self,**kwargs):
        userObj = User.objects.create_superuser(username=kwargs['username'],email=kwargs['email'],password=kwargs['password'])
        return userObj
    def changePassword(self, **kwargs):
        userObj=  User.objects.get(kwargs['username'])
        userObj.set_password(kwargs['password'])
        return userObj
    def removeUser(self, **kwargs):
        userObj = User.objects.get(username=kwargs['username'])
        userObj.set_password(kwargs['password'])
        return userObj
    def addGroup(self):
        pass
    def removeGroup(self):
        pass
    def updateUser(self):
        pass
    def addPremission(self):
        pass
    def removePremission(self):
        pass
    def hasPremision(self):
        pass
    def removeAllPremissions(self):
        pass
    def getAllPremissions(self):
        pass

addNewUser(username=nima,email=nim)