from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Gallery(models.Model):
    photo = models.ImageField(upload_to='pics')

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))

class Profile(models.Model):
    avatarpic = models.ImageField(upload_to='avatar')

    def image_tag_1(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.avatarpic))

class Header(models.Model):
    headerpic = models.ImageField(upload_to='header')

    def image_tag_2(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.headerpic))


class Bio(models.Model):
    bio_text = models.CharField(max_length=5000)
    def __str__(self):
        return self.bio_text

#####################
#     Contact 
#####################

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.CharField(max_length=50)

    def __str__(self):
        return (self.name, self.email, self.phone, self.date)
