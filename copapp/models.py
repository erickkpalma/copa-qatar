from django.db import models

class TabelaModel(models.Model):

    time1 = models.CharField(max_length=10)
    time2 = models.CharField(max_length=10)
    dia = models.IntegerField()
    horario = models.DateTimeField()


    def __str__(self):
        return f'{self.time1} vs {self.time2}'
