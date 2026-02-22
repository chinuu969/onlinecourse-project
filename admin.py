from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Enrollment, Submission, User


# Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Inline for Question inside Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson')


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course')


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Submission)
admin.site.register(User)
