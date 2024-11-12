


from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Hashtag(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0, verbose_name='Цена',null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')

    def __str__(self):
        return self.title