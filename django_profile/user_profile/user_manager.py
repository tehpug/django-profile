from django.contrib.auth.models import User

from models import Group


class UserManager(object):
    def addNewUser(self, **kwargs):
        '''
        >>>addNewUser(username='nima',email='nim4n@yahoo.com',password='nima')
        >>>
        '''
        userObj = User.objects.create_user(username=kwargs['username'],
                                           email=kwargs['email'],
                                           password=kwargs['password'])
        return userObj

    def createSuperUser(self, **kwargs):
        userObj = User.objects.create_superuser(username=kwargs['username'],
                                                email=kwargs['email'],
                                                password=kwargs['password'])
        return userObj

    def changePassword(self, **kwargs):
        userObj = User.objects.get(kwargs['username'])
        userObj.set_password(kwargs['password'])
        return userObj

    def removeUser(self, **kwargs):
        userObj = User.objects.get(username=kwargs['username'])
        userObj.set_password(kwargs['password'])
        return userObj

    def addGroup(self, **kwargs):
        '''
        >>> addGroup(groupName='testGroup',username='morteza')
        '''
        groupObj = Group.objects.get(name=kwargs['groupname'])
        userObj = User.objects.get(username=kwargs['username'])
        userObj.groups.add(groupObj)
        return userObj

    def removeGroup(self, **kwargs):
        '''
        >>> removeGroup(groupName='testGroup',username='morteza')
        '''
        groupObj = Group.objects.get(name=kwargs['groupname'])
        userObj = User.objects.get(username=kwargs['username'])
        userObj.groups.remove(groupObj)
        return userObj

    def updateUser(self, **kwargs):
        pass

    def addPermission(self):
        pass

    def removePermission(self, **kwargs):
        pass

    def hasPermission(self, **kwargs):
        userObj = User.objects.get(username=kwargs['username'])
        userObj.has_perm(kwargs['perms'])
        return userObj

    def removeAllPermissions(self):
        pass

    def getAllPermissions(self):
        pass

# addNewUser(username=nima,email=nim)
