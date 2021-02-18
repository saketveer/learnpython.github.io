from django.db import models
from django.db import migrations, models
 # Create Models Here
class Student(models.Model):
    objects = None
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField(max_length=50)
    stupass = models.CharField(max_length=50)

