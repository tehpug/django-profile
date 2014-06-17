from django.contrib.auth.models import Group


class GroupManager(object):
    def getAllGroups():
        return Group.objects.all()

    def addPremission():
        pass

    def removePremission():
        pass

    def setAllPremissions():
        pass

    def removeAllPremissions():
        pass

    def copyUser():
        pass

    def addUser():
        pass

    def removeUser():
        pass

    def getGroupByName():
        pass

    def getAllPremissions():
        pass
