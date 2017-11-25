"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import school_client.views as school_client


from django.conf.urls import url,include
from school_client.api import TeacherResource,SchoolResource,ExamResource


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^school/', school_client.school),
    url(r'^login/', school_client.login,name='login'),
    url(r'^logout/', school_client.logout,name='logout'),

    url(r'api/school_client/school/', include(SchoolResource.urls())),
    url(r'api/school_client/teacher/', include(TeacherResource.urls())),
    url(r'api/school_client/exam/', include(ExamResource.urls())),
]
