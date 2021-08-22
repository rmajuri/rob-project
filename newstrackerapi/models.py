from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=60, default='')
    link = models.CharField(max_length=2000, default='')
    description = models.CharField(max_length=250, default='')
    image = models.CharField(max_length=2000, default='')

    def _str_(self):
        return self.name
