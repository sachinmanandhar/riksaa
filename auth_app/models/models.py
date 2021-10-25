import os

from django.db import models
from django.conf import settings
from django.db.models.fields import related
from django.contrib.auth.models import AbstractUser

from admin_area.models import Province, Ward, Palika, District
from auth_app.choices import GenderChoices

from auth_app.managers import CustomUserManager

class User(AbstractUser):
    phone_number = models.CharField(max_length=100, unique=True, blank=False, null=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
        
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}'

class RiderType(models.Model):
    type = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return f'{self.type}'

def get_image_path(instance, image):
    _, image_extension = os.path.splitext(image)
    image_name = instance.user.username + image_extension
    return os.path.join("profile_pic", image_name)

def get_document_path(instance, document):
    # _, document_extension = os.path.splitext(document)
    # file_name = instance.user.username + document_extension
    return os.path.join("company_document", instance.user.username, document)

class Rider(models.Model):
    user = models.OneToOneField(
        User,
        related_name='riders',
        related_query_name='rider',
        on_delete=models.CASCADE
    )

    rider_type = models.ForeignKey(
        RiderType,
        related_name='riders',
        related_query_name='rider',
        on_delete=models.CASCADE
    )

    profile_picture = models.ImageField(upload_to=get_image_path, null=False, blank=False)
    valid_docs = models.FileField(upload_to=get_document_path, null=False, blank=False)

    def __str__(self):
        return f'{self.user.username} - {self.rider_type.type}'
    

class Customer(models.Model):

    user = models.OneToOneField(
        User,
        related_name= 'customers',
        related_query_name= 'customer',
        on_delete=models.CASCADE
    )

    profile_picture = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'



class Role(models.Model):
    role = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.role}'

class UserInRole(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete= models.CASCADE, 
        related_name='userinroles',
        related_query_name='userinrole'
    )

    role = models.ForeignKey(
        Role,
        related_name='userinroles',
        related_query_name='userinrole',
        on_delete=models.CASCADE
    )

    gender = models.CharField(max_length=250 ,choices=GenderChoices.choices, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)


    province = models.ForeignKey(
        Province,
        related_name='userinroles',
        related_query_name='userinrole',
        on_delete= models.CASCADE
    )

    district = models.ForeignKey(
        District,
        related_name='userinroles',
        related_query_name='userinrole',
        on_delete=models.CASCADE
    )

    palika = models.ForeignKey(
        Palika,
        related_name='userinroles',
        related_query_name='userinrole',
        on_delete=models.CASCADE
    )

    ward = models.ForeignKey(
        Ward,
        related_name='userinroles',
        related_query_name='userinrole',
        on_delete=models.CASCADE
    )
