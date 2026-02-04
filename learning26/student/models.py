from django.db import models

# Create your models here.


class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge= models.ImageField()
    studentCity= models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)



    class Meta:
        db_table = "student"

class Product(models.Model):
    productName= models.CharField(max_length=100)
    productprice= models.IntegerField()
    productDescription= models.TextField()
    productStock = models.IntegerField(null=True, blank=True)
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)





    class Meta:
        db_table = "product"



class StudentAttendance(models.Model):
    studentName = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=10)  # Present / Absent

    class Meta:
        db_table = "studentAttendance"