from django.db import models

# Create your models here.

class Student(models.Model): #schema is defined with the help of classes.
    # id=models.AutoField() #acts as primary key for the model
    name=models.CharField(max_length=50) #string data is defined in charfield- similar to varchar
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()

class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    number=models.BigIntegerField()

class car(models.Model):
    name=models.CharField(max_length=50)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.name