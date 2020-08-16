from django.db import models
from django.contrib.auth.models import User


class Fet(models.Model):
    name = models.CharField(max_length=120)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Round(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date.strftime("%d/%m/%Y, %H:%M")

    class Meta:
        ordering = ['-date']


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fet = models.ForeignKey(Fet, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    eround = models.ForeignKey(Round, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ': ' + str(self.fet)

    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ['user__first_name', 'user__last_name']
