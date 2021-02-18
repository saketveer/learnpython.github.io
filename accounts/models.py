from django.db import models
from django.db import migrations, models
 # Create Models Here
class employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    status = models.BooleanField()

