from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    # 获取视频分类作为菜单数据
    menu_list = Cate.objects.all()
    # 返回最新的3条数据
    new_list = Video.objects.all().order_by('-create_time')[:3]
    # 返回最热的4条数据
    hot_list = Video.objects.all().order_by('-views')[:4]
    # 返回Vine数据库最新8条数据
    python_list = Video.objects.filter(cate=Cate.objects.get(name='Reaction')).order_by('-create_time')[:8]
    analysis_list_1 = Video.objects.filter(cate=Cate.objects.get(name='Reaction')).order_by('-create_time')[:4]
    analysis_list_2 = Video.objects.filter(cate=Cate.objects.get(name='Reaction')).order_by('-create_time')[4:8]
    analysis_list_3 = Video.objects.filter(cate=Cate.objects.get(name='Reaction')).order_by('-create_time')[8:12]

    gui_list = Video.objects.filter(cate=Cate.objects.get(name='Vine')).order_by('-create_time')[:4]

    web_list = Video.objects.filter(cate=Cate.objects.get(name='抖音')).order_by('-create_time')[:4]

    return render(request, 'index.html', locals())


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
    :return:页数id
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
    :param cateid:页数id
    :return:
    '''
    return HttpResponse('视频{0}页'.format(cateid))
