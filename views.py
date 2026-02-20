from django.http import HttpResponse

def index(request):
    return HttpResponse("Online Course App is working")
from django.shortcuts import render, get_object_or_404
from .models import Course, Submission, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    selected_choices = request.POST.getlist('choice')

    enrollment = request.user.enrollment_set.get(course=course)

    submission = Submission.objects.create(enrollment=enrollment)
    
    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=choice_id)
        submission.choices.add(choice)

    return HttpResponseRedirect(reverse('exam_result', args=(course.id, submission.id)))
def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    total = 0
    score = 0

    for question in submission.enrollment.course.question_set.all():
        total += question.grade
        correct_choices = question.choice_set.filter(is_correct=True)
        selected_choices = submission.choices.filter(question=question)

        if set(correct_choices) == set(selected_choices):
            score += question.grade

    context = {
        'course': submission.enrollment.course,
        'score': score,
        'total': total
    }

    return render(request, 'onlinecourse/exam_result.html', context)


# Create your views here.
