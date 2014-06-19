from django.contrib.auth.models import Group


class GroupManager(object):
    def getAllGroups():
        return Group.objects.all()

    def addPermission():
        pass

    def removePermission():
        pass

    def setAllPermissions():
        pass

    def removeAllPermissions():
        pass

    def copyUser():
        pass

    def addUser():
        pass

    def removeUser():
        pass

    def getGroupByName():
        pass

    def getAllPermissions():
        pass
