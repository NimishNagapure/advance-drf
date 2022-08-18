from django.db import models
from authentication.models import User
# Create your models here.

class Expense(models.Model):
    CATEGORY_OPTIONS = (
        ('ONLINE_SERVISE','ONLINE_SERVISE'),
        ('TRAVEL','TRAVEL'),
        ('FOOD','FOOD'),
        ('RENT','RENT'),
        ('OTHER','OTHER'),
    )

    category = models.CharField(max_length=255,choices=CATEGORY_OPTIONS)
    amount = models.DecimalField(max_digits=10,decimal_places=2,max_length=10)
    description = models.TextField(max_length=255)
    owner = models.ForeignKey(to = User,related_name='expenses',on_delete=models.CASCADE)
    date = models.DateField(null=False,blank=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.owner)+ 's expenses'
            