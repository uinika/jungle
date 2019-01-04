from django.http import HttpResponse

def index(request):
    return HttpResponse("你好，这是一个投票应用！")