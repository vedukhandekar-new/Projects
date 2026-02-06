from django.db import models

# Create your models here.


class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
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
    status = models.CharField(max_length=10)  

    class Meta:
        db_table = "studentAttendance"


class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName    



class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName    


class StudentAcademicInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    semester = models.IntegerField()

    def __str__(self):
        return self.department
    
class StudentLibraryInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    library_card_no = models.CharField(max_length=20)
    issued_books = models.IntegerField(default=0)

    def __str__(self):
        return self.library_card_no
    


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewerName = models.CharField(max_length=100)
    rating = models.IntegerField()
    reviewText = models.TextField()

    class Meta:
        db_table = "productReview"

    def __str__(self):
        return self.product.productName


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    orderDate = models.DateField(auto_now_add=True)
    orderStatus = models.CharField(max_length=20)

    class Meta:
        db_table = "productOrder"

    def __str__(self):
        return self.product.productName
    


class ServiceBooking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customerName = models.CharField(max_length=100)
    bookingDate = models.DateField()
    bookingStatus = models.CharField(max_length=20)

    class Meta:
        db_table = "serviceBooking"

    def __str__(self):
        return self.service.serviceName


class ServiceHistory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    serviceDate = models.DateField()
    serviceStatus = models.CharField(max_length=20)

    class Meta:
        db_table = "serviceHistory"

    def __str__(self):
        return self.service.serviceName
