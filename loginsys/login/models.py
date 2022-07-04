from pyexpat import model
from django.db import models

class encryption_data(models.Model):
  username_in = models.CharField(max_length=255)
  password_in = models.CharField(max_length=255)



