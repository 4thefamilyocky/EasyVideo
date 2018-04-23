#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 批量导入视频数据至数据库
import subprocess
import re
import sys
import os

from django.core.wsgi import get_wsgi_application

sys.path.extend(['/Users/jieyan/project/PycharmProjects/easyvideoproject', ])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easyvideoproject.settings")
application = get_wsgi_application()
import django

django.setup()
from video.models import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, 'media')


def get_duration(filename):
    '''
    获取视频时长
    :param filename:
    :return:
    '''
    s = subprocess.Popen('ffmpeg -i "{0}"'.format(filename), shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    ss = s.stdout.read()

    duration = re.findall(r'Duration:(.*?),', str(ss))[0]
    print(filename, duration)
    return (filename, duration)


def get_video_img(filename):
    '''
    获取视频缩略图
    :param filename:
    :return:
    '''
    s = subprocess.Popen(
        'ffmpeg -i "{0}" -y -f mjpeg -ss 0.5 -t 0.001 -s 320x240 "{1}.jpg"'.format(filename, filename.split('.')[0]),
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return True


# file_dir = 'video/Reaction合集'
# file_dir = 'video/Vine合集'
# file_dir = 'video/快手合集'
file_dir = 'video/抖音合集'


root_dir = os.path.join(BASE_DIR, file_dir)
print(root_dir)
print(os.listdir(root_dir))
print('--' * 50)

for i in os.listdir(root_dir):
    print(file_dir, i)
    # 获取视频信息
    video_duration = get_duration(os.path.join(root_dir, i))
    # 获取缩略图
    img_name = get_video_img(os.path.join(root_dir, i))
    # 插入视频数据
    v = Video.objects.get_or_create(
        name=i.split('.')[0],
        link=os.path.join(file_dir, i),
        img=os.path.join(file_dir, str(i.split('.')[0]) + '.jpg'),
        introduce="抖音合集",
        cate=Cate.objects.get(name='抖音'),
        hour=video_duration[1]
    )
    print('-------->插入视频成功')

    # print('video_duration[1]', video_duration[1])

    # 插入专辑数据
    vv = Video.objects.get(
        name=i.split('.')[0],
        link=os.path.join(file_dir, i),
        img=os.path.join(file_dir, str(i.split('.')[0]) + ".jpg"),
        introduce="抖音合集",
        cate=Cate.objects.get(name='抖音'),
        hour=video_duration[1]
    )
    sets = Set.objects.create(
        name='抖音',
        video=vv
    )
    print('--------> 插入专辑成功')
