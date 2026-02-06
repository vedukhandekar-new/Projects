from django.contrib import admin

# Register your models here.
from .models import Student,Product,StudentAttendance,StudentProfile,Category,Service,StudentAcademicInfo,StudentLibraryInfo,ProductReview,ProductOrder,ServiceBooking,ServiceHistory
# Register your models here.

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(StudentAttendance)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(StudentAcademicInfo)
admin.site.register(StudentLibraryInfo)
admin.site.register(ProductReview)
admin.site.register(ProductOrder)
admin.site.register(ServiceBooking)
admin.site.register(ServiceHistory)
