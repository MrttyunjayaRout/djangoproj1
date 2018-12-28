from django.db import models
class Product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    pcost=models.DecimalField(max_digits=10,decimal_places=10)
    pmfd=models.DateField()
    pexpdt=models.DateField()
