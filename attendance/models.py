from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, help_text='Enter username')
    fname = models.CharField(max_length=200, help_text='Enter first name')
    lname = models.CharField(max_length=200, help_text='Enter last name')
    phone = models.DecimalField(max_digits=13, decimal_places=0, help_text='Enter phone number')
    email = models.EmailField(max_length=254, help_text='Enter email address')

    def __str__(self):
        return [self.username, self.phone, self.email]
