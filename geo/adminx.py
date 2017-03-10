import xadmin
from .models import *


class MiningAreaAdmin(object):
    pass


class ProspectingLineAdmin(object):
    pass


class DrillBaseAdmin(object):
    pass


class DrillLayerAdmin(object):
    pass


class DrillTiltAdmin(object):
    pass


class DrillSamplingAdmin(object):
    pass


xadmin.site.register(MiningArea, MiningAreaAdmin)
xadmin.site.register(ProspectingLine, ProspectingLineAdmin)
xadmin.site.register(DrillBase, DrillBaseAdmin)
xadmin.site.register(DrillLayer, DrillLayerAdmin)
xadmin.site.register(DrillTilt, DrillTiltAdmin)
xadmin.site.register(DrillSampling, DrillSamplingAdmin)
