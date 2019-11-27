from django.db import models

# create you models here:
class testdatabase(models.Model):
    #i tilfælde af man ændrer modellen, så husk "makemigrations"
    Data = models.CharField(max_length=100)
    Timestamp = models.DateTimeField(auto_now='True')
    NODELETE = models.BooleanField(default=False)

    #bliver retuneret hvis man kalder klassen som funktion
    def __str__(self):
        return self.Data


