from django.db import models


class Knight(models.Model):
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Board(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class Field(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    value = models.IntegerField()
