from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Пользователь')
    position_e = models.FloatField(verbose_name='Координата E', default=303801.52280176)
    position_n = models.FloatField(verbose_name='Координата N', default=5872380.4764243)
    status_bar = models.CharField(max_length=200, verbose_name='Состояние', default='Орел')
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Данные' # напр.: Изменить данные
        verbose_name_plural='Данные' 