from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Submission, Choice


def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)

    # create submission
    submission = Submission.objects.create(enrollment=enrollment)

    # get selected choices
    selected_choices = request.POST.getlist('choice')

    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=int(choice_id))
        submission.choices.add(choice)

    submission.save()

    return HttpResponseRedirect(
        reverse('onlinecourse:show_exam_result', args=(course.id, submission.id))
    )


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    total_score = submission.get_score()

    # calculate max possible score
    possible_score = 0
    for question in course.question_set.all():
        possible_score += question.grade

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
