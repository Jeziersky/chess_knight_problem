from django.db import models


class Board(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class Field(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        ordering = ['board', 'value']
