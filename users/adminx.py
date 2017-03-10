# _*_ coding: utf-8 _*_
import xadmin
from xadmin import views
from .models import EmailVerifyRecord


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '矿区数据管理与挖掘平台'
    site_footer = '地盒'


class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)