from django.urls import path
from.import views

urlpatterns=[path('', views.index,name='index'),]
path('course/<int:course_id>/submit/', views.submit_exam, name='submit_exam'),
path('course/<int:course_id>/submission/<int:submission_id>/',
     views.show_exam_result,
     name='exam_result'),
path('course/<int:course_id>/exam/', views.take_exam, name='take_exam'),
