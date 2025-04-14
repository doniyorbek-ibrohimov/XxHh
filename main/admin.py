from django.contrib import admin
from .models import *

class InCorrectInline(admin.TabularInline):
    model=InCorrect
    extra=1

class CorrectAdmin(admin.ModelAdmin):
    inlines = (InCorrectInline,)

admin.site.register(Correct,CorrectAdmin)
admin.site.register(InCorrect)

