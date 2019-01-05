from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "你看到的是问题 %s 的结果。"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("你正在对问题 %s 进行投票。" % question_id)
