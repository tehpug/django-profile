from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Skill(models.Model):
    name = models.CharField(max_length=50)

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile')
    bio = models.TextField()
    skills = models.ManyToManyField(Skill)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sessions = models.IntegerField(default=0)


########## An interceptor to create profile for every user who is created automatically
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
#######################################################################################


# class Friends(models.Model):
#     userF = models.ForeignKey(PugUsers, related_name="userF")
#     userFriend = models.ForeignKey(PugUsers, related_name="user_Friend")
#     friendshipDate = models.DateTimeField(auto_now=True)

# class Message(models.Model):
#     userSender = models.ForeignKey(PugUsers, related_name="user_sender")
#     userReceiver = models.ForeignKey(PugUsers, related_name="user_receiver")
#     mesSubject = models.CharField(max_length=100)
#     mesBody = models.CharField(max_length=1000)




class Social(models.Model):
    user = models.ForeignKey(UserProfile)
    site = models.IntegerField(max_length=20)
    user_link = models.URLField(max_length=70)


class Presentaion(models.Model):
    user = models.ForeignKey(UserProfile)
    presentaion_link = models.URLField(max_length=70)
    like = models.IntegerField()


