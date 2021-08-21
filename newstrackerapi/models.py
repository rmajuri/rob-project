from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=60, default='')
    link = models.CharField(max_length=2000)
    description = models.CharField(max_length=250)

    def _str_(self):
        return self.name
