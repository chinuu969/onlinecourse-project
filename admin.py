
from django.contrib import admin
from.models import Question,Choice,Submission,Enrollment,Course

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Course)
# Register your models here.
