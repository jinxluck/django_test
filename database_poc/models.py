from django.db import models

# create you models here:

class testdatabase(models.Model):
    Data = models.CharField(max_length=100)

    def __str__(self):
        return self.Data


