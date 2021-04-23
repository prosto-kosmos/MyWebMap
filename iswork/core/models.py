from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name='Пользователь')
    position_e = models.FloatField(verbose_name='Координата E', default=4016594.740906363)
    position_n = models.FloatField(verbose_name='Координата N', default=6977780.708997443)
    zoom = models.FloatField(verbose_name='Приближение', default=11)
    settings_size_text = models.IntegerField(verbose_name='Масштаб текста списка датчиков', default=12)
    settings_size_preview = models.IntegerField(verbose_name='Масштаб превью видеопотока', default=150)
    settings_opacity_windows = models.FloatField(verbose_name='Прозрачность окон указателей', default=1.0)
    
    def __str__(self):
        return f'Данные пользователя {self.user.username} ({self.position_e}, {self.position_n})'

    class Meta:
        verbose_name='Данные' # напр.: Изменить данные
        verbose_name_plural='Данные' 