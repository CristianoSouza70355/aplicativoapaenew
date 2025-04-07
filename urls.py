"""
URL configuration for apae_frequency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from attendance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('alunos/', views.student_list, name='student_list'),
    path('frequencia/', views.attendance_register, name='attendance_register'),
    path('marcar-frequencia/', views.mark_attendance, name='mark_attendance'),
    path('gerar-relatorio/', views.generate_report, name='generate_report'),
    path('exportar-pdf/', views.export_pdf, name='export_pdf'),
    path('alunos/<int:student_id>/delete/', views.delete_student, name='delete_student'),
]
