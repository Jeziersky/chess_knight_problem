from django.db import models


class Knight(models.Model):
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
