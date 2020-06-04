from django.test import TestCase
from . models import *
from .models import Image,Profile

# Create your tests here.
class ImageTestClass(TestCase):
    '''
    This is a class that perform unnittest  behaviour on the Image Model.
    '''
    
    def setUp(self):
        
        self.image_one = Image(image='images/trump.jpeg',image_name='trump', image_caption='blacks lives matter',likes=200, id=1,user_id=3)
        
    def test_instance(self):
        Image.objects.all().delete()
        self.assertTrue(isinstance(self.image_one,Image)) 

    def test_save_method(self):
        
        self.image_one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) is 0)
        
    def test_update_method(self):
        self.image_one.save()
        new_caption = 'Trump a disgrace to humanity'
        done = self.image_one.update_caption(self.image_one.id,new_caption)
        self.assertEqual(done,new_caption)
        
    def tearDown(self):
        Image.objects.all().delete()   


class ProfileTestClass(TestCase):
    
    '''
    This is a class that perform unnittest  behaviour on the Profile Model.
    '''
    
    def setUp(self):
        self.profile_one = Profile(profile_photo='images/coder.jpg',bio='Currently junior dev is the stage am in my career',user_id=3)
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile_one,Profile)) 

    def test_save_method(self):
        
        self.profile_one.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile_one.save_profile()
        self.profile_one.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) is 0)
        
    def test_update_method(self):
        self.profile_one.save_profile()
        new_bio = '# blacks lives matter'
        done = self.profile_one.update_bio(self.profile_one.pk,new_bio)
        self.assertEqual(done,new_bio)
        
    def tearDown(self):
        Profile.objects.all().delete()
    


