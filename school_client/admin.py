#_*_encoding:utf-8
from django.contrib import admin

# Register your models here.
from school_client.models import Teacher,School,Exam

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school', )
    search_fields = ('teacher',)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')

class ExamAdmin(admin.ModelAdmin):
    list_display = ('id','name','start','end','total','shui','place',)



admin.site.register(Teacher,TeacherAdmin)
admin.site.register(School,SchoolAdmin)
admin.site.register(Exam,ExamAdmin)
