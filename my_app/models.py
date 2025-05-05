from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=100)
    weight=models.IntegerField(default=0)
    height=models.IntegerField(default=0)
    gender=models.CharField(max_length=100,default='male''female')
    dob=models.DateField(null=True, blank=True)



    class Meta:
        db_table ='customer'





































#  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)


# python manage.py makemigrations
#python manage.py migrate