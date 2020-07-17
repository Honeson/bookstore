from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.



class CustomUserTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'sunny',
            email = 'sunny@email.com',
            password = 'testsunny'
        )

        self.assertEqual(user.username, 'sunny')
        self.assertEqual(user.email, 'sunny@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'admin',
            email = 'email@admin.com',
            password = 'adminpass'
        )

        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'email@admin.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)