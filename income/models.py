from django.db import models
from authentication.models import User
# Create your models here.

class Income(models.Model):
    SOURCE_OPTIONS = (
        ('SALARY','SALARY'),
        ('BUSINESS','BUSINESS'),
        ('FOOD','FOOD'), 
        ('SIDE-HUSTLES','SIDE-HUSTLES'),
        ('OTHER','OTHER'),
    )

    source = models.CharField(max_length=255,choices=SOURCE_OPTIONS)
    amount = models.DecimalField(max_digits=10,decimal_places=2,max_length=10)
    description = models.TextField(max_length=255)
    owner = models.ForeignKey(to = User,related_name='income',on_delete=models.CASCADE)
    date = models.DateField(null=False,blank=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.owner)+ 's income'
