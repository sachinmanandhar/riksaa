from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

class Province(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

class District(models.Model):
    province = models.ForeignKey(
        Province, 
        related_name='districts',
        related_query_name='district',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

class Palika(models.Model):
    province = models.ForeignKey(
        Province, 
        related_name='palikas', 
        related_query_name='palika',
        on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District,
        related_name='districts',
        related_query_name='district',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

class Ward(models.Model):
    province = models.ForeignKey(
        Province,
        related_name = 'wards',
        related_query_name = 'ward',
        on_delete= models.CASCADE
    )
    district = models.ForeignKey(
        District,
        related_name = 'wards',
        related_query_name= 'ward',
        on_delete= models.CASCADE
    )
    palika = models.ForeignKey(
        Palika,
        related_name='wards',
        related_query_name= 'ward',
        on_delete=models.CASCADE
    )

    number = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.province.name} - {self.district.name} - {self.number}'
    