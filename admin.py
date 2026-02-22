
from django.contrib import admin
from.models import Question,Choice,Submission,Enrollment,Course,Lesson,User

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)

# Register your models here.
