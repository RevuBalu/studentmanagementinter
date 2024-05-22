"""
URL configuration for studentmanagementsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from management import views

app_name="management"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('principlesignup',views.principlesignup,name="principlesignup"),
    path('teachersignup',views.teachersignup,name="teachersignup"),
    path('studentsignup',views.studentsignup,name="studentsignup"),
    path('login',views.user_login,name='login'),
    path('principlehome',views.principlehome,name='principlehome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('logout',views.user_logout,name='logout'),
    path('studentsview',views.studentsview,name='studentsview'),
    path('teachersview',views.teachersview,name='teachersview'),
    path('studentdetail/<int:p>',views.studentdetail,name='studentdetail'),
    path('teacherdetail/<int:p>',views.teacherdetail,name='teacherdetail'),
    path('studentupdate/<int:p>',views.studentupdate,name='studentupdate'),
    path('teacherupdate/<int:p>',views.teacherupdate,name='teacherupdate'),
    path('studentdelete/<int:p>',views.studentdelete,name='studentdelete'),
    path('teacherdelete/<int:p>',views.teacherdelete,name='teacherdelete'),
]
