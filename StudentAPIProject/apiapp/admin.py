from django.contrib import admin
from apiapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["rollno", "name", "marks", "addr"]

admin.site.register(Student,StudentAdmin)
