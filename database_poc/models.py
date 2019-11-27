from django.db import models

# create you models here:

class testdatabase(models.Model):
    Data = models.CharField(max_length=100)
    Timestamp = models.DateTimeField(auto_now='True')
    NODELETE = models.BooleanField(default=False)

    def __str__(self):
        return self.Data


