from django.contrib import admin

from .models import Cours
from .models import CasCliniques

admin.site.register(Cours)
admin.site.register(CasCliniques)