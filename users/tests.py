from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


from .forms import CustomUserCreationForm
from .views import SignupPageView

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


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hey you, what are you doing here')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)