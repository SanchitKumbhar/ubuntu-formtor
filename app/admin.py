from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(FormInfo)
admin.site.register(FormData)
admin.site.register(DraftModel)
admin.site.register(Answers)
