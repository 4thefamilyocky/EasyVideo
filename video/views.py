from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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

    kuaishou_list = Video.objects.filter(cate=Cate.objects.get(name='快手')).order_by('-create_time')[:4]

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
    menu_list = Cate.objects.all()
    # 获取视频数据
    id = int(vid)
    video = Video.objects.get(id=vid)
    # 获取视频专辑
    try:
        set_name = Set.objects.get(video=id).name
        video_set = Set.objects.filter(name=set_name)
    except:
        random_video = Video.objects.order_by('?')[:5]
    # 增加访问人数
    try:
        video.views += 1
        video.save()
    except Exception as e:
        print(e)
    # 获取点赞人数
    try:
        likes = Likes.objects.filter(video=video).count()
    except:
        likes = 0
    # 添加观看记录
    try:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            history = History.objects.create(user=user, video=video)
            history.save()
    except Exception as e:
        print(e)
    return render(request, 'single.html', locals())


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
    menu_list = Cate.objects.all()
    cate_id = Cate.objects.get(id=cateid)
    video_list = Video.objects.filter(cate=cate_id)
    cate_video_list = getPage(request, video_list)
    return render(request, 'cate.html', locals())


def getPage(request, video_list):
    '''
    分页罗辑
    :param request:
    :param video_list:
    :return:
    '''
    paginator = Paginator(video_list, 12)
    try:
        page = int(request.GET.get('page', 1))
        video_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        video_list = paginator.page(1)
    return video_list


@login_required
def like(request):
    '''
    视频功能
    :param request:
    :return:
    '''
    if request.method == 'POST':
        videoid = request.POST.get("vid")
        video = Video.objects.get(id=videoid)
        user = request.user
        try:
            Likes.objects.get_or_create(
                user=user,
                video=video,
            )
            # InfoKeep.save()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False})
    else:
        return JsonResponse({"success": False})
