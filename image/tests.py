from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Setup method
    def setUp(self):
        self.location = Location(location='china')
        self.location.save()
        
        self.category = Category(category = 'streetshoot')
        self.category.save()
        
        self.image = Image(pic_image = 'pic1.jpg', name='test',description='This is a test image',location = self.location, image_category = self.category)
        
        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    # testing the save method
    def test_save_method(self):
        self.image = Image(pic_image = 'pic1.jpg', name='test',description='This is a test image',location = self.location, image_category = self.category)
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >= 1)
        
    def test_delete_method(self):
        self.image = Image(pic_image = 'pic1.jpg', name='test',description='This is a test image',location = self.location, image_category = self.category)
        self.image.save_image()
        images = self.image.delete_image()
        deleted = Image.objects.all()
        self.assertTrue(len(deleted) <= 0)
        
class LocationTestClass(TestCase):
    # SetUp Class
    def setUp(self):
        self.location = Location(location="china")
        
    def tearDown(self):
        Location.objects.all().delete()
        
    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>= 1)
        
class CategoryTestClass(TestCase):
    # SetUp Class
    def setUp(self):
        self.category = Category(category="streetshoot")
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>= 1)
        
    def test_delete_category(self):
        self.category.save_category()
        categories = self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)