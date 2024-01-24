from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Plans)
admin.site.register(PlansEquipment)
admin.site.register(PlansOption)
admin.site.register(PlansPeriod)
admin.site.register(PlansSpeed)
