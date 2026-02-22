from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [

    # take exam
    path(
        'course/<int:course_id>/exam/',
        views.take_exam,
        name='take_exam'
    ),

    # submit exam
    path(
        'course/<int:course_id>/submit/',
        views.submit_exam,
        name='submit_exam'
    ),

    # show exam result  ⭐ REQUIRED
    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]
