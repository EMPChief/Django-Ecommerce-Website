from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    price = models.FloatField()
    price_cents = models.IntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} | {self.price} | {self.created_at}'
    
    def save(self, *args, **kwargs):
        self.price_cents = int(self.price * 100)
        super().save(*args, **kwargs)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'
    
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
    
    def get_rating(self):
        reviews = self.review.all()
        total_rating = 0
        for review in reviews:
            total_rating += review.rating
        if reviews:
            return total_rating / len(reviews)
        else:
            return 0

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.created_by} | {self.created_at} | {self.rating} | {self.product}'

@receiver(pre_save, sender=Product)
def update_price_cents(sender, instance, **kwargs):
    instance.price_cents = int(instance.price * 100)
