from django.db import models

# to translate model fields, use ugettext_lazy
from django.utils.translation import ugettext_lazy as _


class SubModel(models.Model):
    basic = models.ForeignKey("BasicModel", on_delete=models.PROTECT)
    name = models.CharField(verbose_name=_("Название"), max_length=32)


class BasicModel(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=32)
    text = models.TextField(verbose_name=_("Текст"))
    info = models.CharField(verbose_name=_("Информация"), max_length=64)

    class Meta:
        verbose_name = _("Базовая модель")
        verbose_name_plural = _("Базовые модели")
