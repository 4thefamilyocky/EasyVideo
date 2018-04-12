from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    return HttpResponse('首页')


def login(request):
    '''
    登录页面
    :param request:
    :return:
    '''
    return HttpResponse('登录')


def register(request):
    '''
    注册页面
    :param request:
    :return:
    '''
    return HttpResponse('注册')


# 注意!类似vid的参数一定要加上
def videoDetail(request, vid):
    '''
    视频详情
    :param request:
    :return:
    '''
    return HttpResponse('视频{0}详情'.format(vid))


def viewHistory(request):
    '''
    视频观看历史
    :param request:
    :return:
    '''
    return HttpResponse('视频观看历史')


def videoCate(request, cateid):
    '''
    视频分页
    :param request:
    :param cateid:
    :return:
    '''
    return HttpResponse('视频{0}页'.format(cateid))
