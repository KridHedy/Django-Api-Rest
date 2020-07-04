from django.db import models

class Customer(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    gender = models.CharField(max_length=10)
    company = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    title = models.CharField(max_length=60,null=True)
    latitude = models.IntegerField( default=0,null=True)
    longitude = models.IntegerField( default=0,null=True)
    def __str__(self):
        return self.id

    
