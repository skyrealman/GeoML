# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class MiningArea(models.Model):
    name = models.CharField(verbose_name='矿区名称', max_length=50, default='矿区')
    code = models.CharField(verbose_name='矿区编码', max_length=10)
    type = models.CharField(verbose_name='矿种类型', max_length=10)
    area = models.CharField(verbose_name='所在地', max_length=20)
    content = models.TextField(verbose_name='矿区描述', null=True)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '矿区信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ProspectingLine(models.Model):
    code = models.CharField('勘探线号', max_length=10)
    miningArea = models.ForeignKey(MiningArea, verbose_name='所属矿区', on_delete=models.CASCADE)
    coord_x = models.FloatField('X坐标', null=False)
    coord_y = models.FloatField('Y坐标', null=False)
    coord_z = models.FloatField('Z坐标', null=False)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '勘探线信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s%s' % ('勘探线', self.code)


class DrillBase(models.Model):
    code = models.CharField('钻孔编号', max_length=10)
    coord_x = models.FloatField('X坐标', null=False)
    coord_y = models.FloatField('Y坐标', null=False)
    coord_z = models.FloatField('Z坐标', null=False)
    depth = models.FloatField('总深度', null=False)
    prospectingLine = models.ForeignKey(ProspectingLine, verbose_name='所属勘探线', on_delete=models.CASCADE)
    miningArea = models.ForeignKey(MiningArea, verbose_name='所属矿区', on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '钻孔基本信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s%s' % ('钻孔', self.code)


class DrillLayer(models.Model):
    code = models.CharField('分层编号', max_length=10)
    drillBase = models.ForeignKey(DrillBase, verbose_name='所属钻孔', on_delete=models.CASCADE)
    layer_name = models.CharField(verbose_name='分层名称', max_length=10)
    layer_des = models.TextField('分层描述', null=True)
    top = models.FloatField('顶深')
    bottom = models.FloatField('底深')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '钻孔分层信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s_%s' % (self.drillBase.code, self.code)


class DrillTilt(models.Model):
    drillBase = models.ForeignKey(DrillBase, verbose_name='所属钻孔', on_delete=models.CASCADE)
    depth = models.FloatField('顶深')
    zenith = models.FloatField('顶角')
    azimuth = models.FloatField('方位角')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '钻孔测斜信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.drillBase.code


class DrillSampling(models.Model):
    code = models.CharField('取样编号', max_length=10)
    drillBase = models.ForeignKey(DrillBase, verbose_name='所属钻孔', on_delete=models.CASCADE)
    d_from = models.FloatField('自')
    d_to = models.FloatField('至')
    length = models.FloatField('长度')
    element1 = models.FloatField('元素一')
    element2 = models.FloatField('元素二')
    element3 = models.FloatField('元素三')
    element4 = models.FloatField('元素四')
    element5 = models.FloatField('元素五')
    element6 = models.FloatField('元素六')
    element7 = models.FloatField('元素七')
    element8 = models.FloatField('元素八')
    element9 = models.FloatField('元素九')
    element10 = models.FloatField('元素十')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '钻孔取样信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code
