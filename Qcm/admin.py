from django.contrib import admin

# Register your models here.

from .models import Qcm
from .models import Question
from .models import Choice


admin.site.register(Qcm)
admin.site.register(Question)
admin.site.register(Choice)