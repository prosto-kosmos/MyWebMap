from django.db import models
from django.contrib.auth.models import User
import json

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

class Settings(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Пользователь')
    entity_id = models.CharField(verbose_name='Идентификатор объекта', primary_key=True, max_length=50)
    visibility = models.BooleanField(verbose_name='Отображение указателя', default=True)
    shown_param = models.BooleanField(verbose_name='Отображение списка параметров', default=False)
    shown_preview = models.BooleanField(verbose_name='Отображение окна с превью', default=False)
    hidden_params_ids = models.TextField(verbose_name='Список идентификаторов скрытых параметров', default=json.dumps([]))
    shown_stream_ids = models.TextField(verbose_name='Список идентификаторов отображаемых видеопотоков', default=json.dumps([]))

    def __str__(self):
        return f'Настройки пользователя {self.user.username} (объект {self.entity_id})'

    class Meta:
        verbose_name='Настройки' # напр.: Изменить данные
        verbose_name_plural='Настройки' 