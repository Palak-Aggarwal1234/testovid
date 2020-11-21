from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ReportDb(models.Model):
    Test1 = models.BooleanField(default=False)
    Test2 = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "Task1:%s Task2:%s"%(self.Test1, self.Test2)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
