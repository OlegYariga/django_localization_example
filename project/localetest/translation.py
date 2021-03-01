from modeltranslation.translator import translator, TranslationOptions
from .models import BasicModel, SubModel


class BasicModelTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


class SubModelTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(BasicModel, BasicModelTranslationOptions)
translator.register(SubModel, SubModelTranslationOptions)
