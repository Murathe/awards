from django.test import TestCase
from .models import Profile,Projects,Rates


class ProfileTestClass(TestCase):
    def setUp(self):
        self.murathe = Profile(profile_photo='def.jpg',bio='Murathe is a gem', phone_number='0722100100')

    def test_instance(self):
        self.assertTrue(isinstance(self.murathe,Profile))

    def test_save(self):
        self.murathe.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
 
