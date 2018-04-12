from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    '''
    首页视图
    :param request:
    :return:
    '''
    return HttpResponse('这是首页')
