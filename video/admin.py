from django.contrib import admin
from .models import *


# Register your models here.
class CateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'img', 'passwd', 'cate', 'views', 'create_time', 'status']
    list_editable = ['status', 'passwd']
    list_filter = ['cate', 'status']
    search_fields = ['introduce']


class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'video', 'lable']


class SetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'video']
    list_filter = ['name']


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'video', 'view_date']
    list_filter = ['user', 'video', 'view_date']


admin.site.register(Cate, )
admin.site.register(Video, )
admin.site.register(Label, )
admin.site.register(Set, )
admin.site.register(History, )
