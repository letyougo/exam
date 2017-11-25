from django.shortcuts import render

# Create your views here.


from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required

from django.views.generic import DetailView



from school_client.models import School

from django.views.generic import TemplateView
from school_client.models import Teacher


class school(TemplateView):
    template_name = "school.html"
    model = Teacher



