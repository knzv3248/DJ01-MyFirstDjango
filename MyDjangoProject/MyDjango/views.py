from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django </h1>")

def my_data(request):
    return HttpResponse("<h1>Это страница 'data' моего первого проекта на Django </h1>")

def my_test(request):
    return HttpResponse("<h1>Это страница 'test' моего первого проекта на Django </h1>")
