from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class ProfileTestCase(TestCase):
    def test_creating_user_will_create_profile(self):
        user = User(username='test', email='test@test.com')
        user.set_password('test')
        user.save()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.profile)
        self.assertIs(0, user.profile.sessions)

