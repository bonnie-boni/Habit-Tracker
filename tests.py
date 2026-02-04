from django.test import TestCase
from django.contrib.auth.models import User
from habits.models import Habit


class HabitModelTest(TestCase):
    """Test Habit model"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_create_build_habit(self):
        """Test creating a build habit"""
        habit = Habit.objects.create(
            user=self.user,
            habit_type='build',
            category='reading',
            name='Read daily'
        )
        self.assertEqual(habit.name, 'Read daily')
        self.assertEqual(habit.habit_type, 'build')
        self.assertTrue(habit.is_active)

    def test_create_drop_habit(self):
        """Test creating a drop habit"""
        habit = Habit.objects.create(
            user=self.user,
            habit_type='drop',
            category='addiction',
            name='Quit smoking'
        )
        self.assertEqual(habit.habit_type, 'drop')


class UserProfileTest(TestCase):
    """Test UserProfile functionality"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_profile_creation(self):
        """Test user profile is created"""
        from users.models import UserProfile
        profile = UserProfile.objects.create(
            user=self.user,
            display_name='Test User',
            theme_preference='dark'
        )
        self.assertEqual(profile.display_name, 'Test User')
        self.assertEqual(profile.theme_preference, 'dark')
