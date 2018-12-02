from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    umail = models.EmailField(max_length=255,unique=True)

    def __str__(self):
        return self.fname
