from django.test import TestCase
from afp2.models import  RegisterUser


class RegisterUserTestCase(TestCase):
    def setUp(self):
        RegisterUser.objects.create(username="test11", fullname="testUser11", password="testPw11", email="testmail11@tesztmail.teszt",dateOfBirth="1998-01-11")
        RegisterUser.objects.create(username="test13", fullname="testUser13", password="testPw13", email="testmail13@tesztmail.teszt",dateOfBirth="1998-01-13")

    def testRegisteredUsers(self):
        test11 = RegisterUser.objects.get(username="test11")
        test13 = RegisterUser.objects.get(username="test13")
        self.assertEqual(test11.fullname, 'testUser11')
        self.assertFalse(test13.fullname, 'testUser12')