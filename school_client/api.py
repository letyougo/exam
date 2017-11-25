from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer,SubPreparer,CollectionSubPreparer

from .models import Teacher,School,Exam
from django.contrib.auth.models import User

class TeacherResource(DjangoResource):
    paginate = True
    page_size = 10
    school_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'school': SubPreparer('school',school_preparer),
        'province': 'province',
        'location': 'location',
        'idcard':'idcard',
        'sex':'sex'
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated()

    # GET /api/posts/ (but not hooked up yet)
    def list(self):
        user_id = self.request.user.id
        school = School.objects.get(user_id=user_id)
        return Teacher.objects.filter(school=school)

    # GET /api/posts/<pk>/ (but not hooked up yet)
    def detail(self, pk):
        return Teacher.objects.get(id=pk)

    def delete(self, pk):
        Teacher.objects.get(id=pk).delete()






class SchoolResource(DjangoResource):



    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated()

    # GET /api/posts/ (but not hooked up yet)
    def list(self):
        return School.objects.all()

    # GET /api/posts/<pk>/ (but not hooked up yet)
    def detail(self, pk):
        return School.objects.get(id=pk)

    def delete(self, pk):
        School.objects.get(id=pk).delete()



class ExamResource(DjangoResource):


    teacher_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name':'name',
        'sex':'sex',

    })

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'teacher':CollectionSubPreparer('teacher.all',teacher_preparer),
        'place':'place',
        'start':'start',
        'end':'end',
        'total':'total',
        'shui':'shui'
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated()

    # GET /api/posts/ (but not hooked up yet)
    def list(self):
        return Exam.objects.all()

    # GET /api/posts/<pk>/ (but not hooked up yet)
    def detail(self, pk):
        return Exam.objects.get(id=pk)

    def delete(self, pk):
        Exam.objects.get(id=pk).delete()
