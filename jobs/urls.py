from django.urls import path

from . import views

urlpatterns = [
    path('sabuj/',views.about, name='about'),
    path('sabuj/jobs/<int:job_id>/', views.detail,name='detail'),
]