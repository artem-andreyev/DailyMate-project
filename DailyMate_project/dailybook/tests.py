from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Dailybook


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view_with_valid_credentials(self):
        data = {
            'username': 'testuser',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        }

        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)

        self.assertEqual(response.url, reverse('profile'))

    def test_register_view_with_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password1': 'StrongPassword123!',
            'password2': 'DifferentPassword123!',
        }

        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_register_view_with_existing_username(self):
        User.objects.create_user(username='teo', password='StrongPassword123!')

        data = {
            'username': 'teo',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123',
        }

        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors['username'][0],
                         'A user with that username already exists.')

    def test_register_view_with_short_password(self):
        data = {
            'username': 'testuser',
            'password1': '123',
            'password2': '123',
        }

        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors['password2'][0],
                         'This password is too short. It must contain at least 8 characters.')


class TestDailybookCreateView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='StrongPassword123!')

    def test_dailybook_create_view_with_authenticated_user(self):
        self.client.login(username='testuser', password='StrongPassword123!')

        data = {
            'title': 'Test Title',
            'content': 'Test Content',
            'emotion': 'happy',
            'date_edit': '2020-03-03',
        }

        response = self.client.post(reverse('dailybook_create', kwargs={'username': 'testuser'}), data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dailybook.objects.filter(title='Test Title').exists())

    def test_dailybook_create_view_with_unauthenticated_user(self):
        data = {
            'title': 'Test Title',
            'content': 'Test Content',
            'emotion': 'happy',
            'date_edit': '2020-03-03',
        }

        response = self.client.post(reverse('dailybook_create', kwargs={'username': 'testuser'}), data)

        self.assertEqual(response.status_code, 302)
