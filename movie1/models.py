from django.contrib.auth.models import User
from django.db import models


class Matrix(models.Model):
    Row = models.IntegerField()
    Column = models.IntegerField()
    auth = models.ForeignKey(User, default=None, on_delete=None)
    Select_Dimension = models.TextField(default='Row')
    Data = models.CharField(max_length=1000, default=None)

    def __int__(self):
        return self.Row.Column

    def __str__(self):
        return self.Select_Dimension
