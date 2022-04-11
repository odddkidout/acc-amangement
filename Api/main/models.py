from django.db import models

class Acc(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    cookie = models.CharField(max_length=1000)
    ip = models.CharField(max_length=50)
    suscription = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class LockedAcc(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    cookie = models.CharField(max_length=1000, null=True)
    ip = models.CharField(max_length=50,null=True)
    suscription = models.CharField(max_length=50,null=True)
    Country = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name



