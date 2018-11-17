from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(ClassSchedule)
admin.site.register(AttendanceData)



