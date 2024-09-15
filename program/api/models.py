from django.db import models


class Massage(models.Model):
    massage = models.CharField(max_length=100)

    def __str__(self):
        return self.massage