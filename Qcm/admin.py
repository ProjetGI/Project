from django.contrib import admin

# Register your models here.

from .models import Qcm
from .models import Question


admin.site.register(Qcm)
admin.site.register(Question)
