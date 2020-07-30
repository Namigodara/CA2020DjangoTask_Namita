from django.db import models

class Info(models.Model):
    Name = models.CharField("Full Name", max_length = 50)
    ID = models.EmailField("Email ID", max_length = 75)
    Contact = models.PositiveIntegerField("Contact Number",max_length = 10)
    Address = models.CharField( max_length = 400)

