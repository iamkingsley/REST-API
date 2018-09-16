from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase): 
    def setUp(self): 
        user =  User.objects.create(username='shirleycodjoe', email='shirleycodjoe@gmail.com')
        user.set_password("Admin@123")
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='shirleycodjoe')
        self.assertEqual(qs.count(), 1)