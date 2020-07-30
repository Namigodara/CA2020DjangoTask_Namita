from django.db import models

class Info(models.Model):
    Name = models.CharField("Full Name", max_length = 50)
    email = models.EmailField("Email address", max_length = 75)
    Contact = models.IntegerField("Contact Number")
    Address = models.CharField( max_length = 400)

