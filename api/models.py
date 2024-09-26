from django.contrib.auth.models import User
from django.db import models
import uuid


# Добавить таблицу Люди(клиенты, персонал), Категории, добавить поля цена и связи между всем этим Foring
# CRUD с помощью сериализаторов
# Точки входа (ентри поинт)
# Релейшены
class Categories(models.Model):
    uuid = models.UUIDField(primary_key=True, verbose_name='Идентификационный номер человека', default=uuid.uuid4)
    name = models.CharField(max_length=100, verbose_name='Название категории')
    # Связь OneToMenu с massage


class Massage(models.Model):
    uuid = models.UUIDField(primary_key=True, verbose_name='Идентификатор записи', default=uuid.uuid4)
    name = models.CharField(max_length=100, null=True, default=None)
    price = models.DecimalField(default=1.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    categories = models.ForeignKey(Categories, related_name='massage', on_delete=models.CASCADE, default=None)

    # Связь с людьми, у которых есть флаг

    def __str__(self):
        return f'Товар: {self.name}. Цена: {self.price}'

    def __unicode__(self):
        return '%d: %s' % (self.uuid, self.name)


class People(User):
    # uuid = models.UUIDField(primary_key=True, verbose_name='Идентификационный номер человека', default=uuid.uuid4)
    # name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    flag_user = models.BooleanField(verbose_name='Флаг пользователя')
    massage = models.ForeignKey(Massage, related_name='people', on_delete=models.CASCADE, default=False)
    def __str__(self):
        return f'Имя пользователя: {self.username}, Флаг пользователя: {self.flag_user} '

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.username)