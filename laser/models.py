from django.db import models
from django.contrib.auth.models import User


class EntryLaser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fet = models.CharField(max_length=120)
    navigo = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.fet)

    class Meta:
        verbose_name_plural = 'Entries'
