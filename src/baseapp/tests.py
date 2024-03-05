from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        """Test that a user can register successfully with valid data."""
        self.assertEqual(User.objects.count(), 0)
        
        url = reverse('signup')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'ComplexPassword!123',
            'password2': 'ComplexPassword!123',
        }
        
        response = self.client.post(url, data)
        
        self.assertRedirects(response, reverse('login'), status_code=302, target_status_code=200)
        
        self.assertEqual(User.objects.count(), 1)
        
        user = User.objects.first()
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertTrue(user.check_password(data['password1']))