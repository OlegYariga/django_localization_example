# to register translation we have to import .translation file first
from .translation import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.contrib import admin

from .models import BasicModel, SubModel
from . import forms


class SubModelAdminInline(TranslationTabularInline):
    model = SubModel


class BasicModelAdmin(TranslationAdmin):
    form = forms.BasicForm
    # all fields that need to be translated, will be changed to field_name+lang
    # thus, these field tuple will be look like fields = ('name_ru', 'name_en', 'text_ru', 'text_en', 'info')
    fields = ('name', 'text', 'info')
    list_display = ('name',)
    inlines = (SubModelAdminInline,)


admin.site.register(BasicModel, BasicModelAdmin)
