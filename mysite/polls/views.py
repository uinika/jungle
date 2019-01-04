from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("你正在查看问题 %s 。" % question_id)


def results(request, question_id):
    response = "你看到的是问题 %s 的结果。"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("你正在对问题 %s 进行投票。" % question_id)
