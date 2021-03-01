# django-localization-example

Project template designed for the introduction in usage Django internalization utilities. Using django translation 
and django modeltranslation you will be able to localize all static and dynamic (in the database) texts in your project.

## Requirements

- python >3.4
- django >2.0
- django-modeltranslation >0.13

## Translate static texts

### Setup languages

In **settings.py** add localization settings:
```python
LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
```
and then create **locale** folder in project root.

### Translate texts in project

To translate static texts in views, use **ugettext** or **gettext** functions. Before request, activate 
selected language:
```python
from django.utils.translation import ugettext as _
...

request.LANGUAGE_CODE = request.GET.get('language', 'ru')
activate(language=request.GET.get('language', 'ru'))
...

some_text = _("Привет, мир!")
```
### Translate texts using in admin page (e.g.: verbose names or help texts)

To translate texts in admin panel, use **ugettext_lazy** or **gettext_lazy**:
```python
from django.utils.translation import ugettext_lazy as _
...

class SomeModel(models.Model):
    info = models.CharField(verbose_name=_("Информация"), max_length=64)

    class Meta:
        verbose_name = _("Базовая модель")
        verbose_name_plural = _("Базовые модели")
```

### Make and compile messages

Run `python manage.py makemessage -l en` (or `django-admin makemessage -l en`) to create gettext file with selected
language.

Then translate messages in file `locale/en/django.po` in `msgstr` string:
```python
#: project/models.py:9
msgid "Информация"
msgstr "Information"

#: project/models.py:12
msgid "Базовая модель"
msgstr "Basic model"

#: project/models.py:13
msgid "Базовые модели"
msgstr "Basic models"

#: project/views.py:11
msgid "Привет, мир!"
msgstr "Hello, world!"
```

_After these steps you will get translated text, when you pass get parameter language=en in your view_

## Translate dynamic texts in admin

1. In your app directory create file named **translation.py**.
2. Create and register translation:
```python
from modeltranslation.translator import translator, TranslationOptions
from .models import BasicModel, SubModel


class BasicModelTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
...

translator.register(BasicModel, BasicModelTranslationOptions)
```
3. Make and apply migrations
4. Then import your translation file in **admin.py** in your app and
register admin page:
```python
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.contrib import admin

from .models import BasicModel

class BasicModelAdmin(TranslationAdmin):
    fields = ('name', 'text', 'info')
    list_display = ('name',)


admin.site.register(BasicModel, BasicModelAdmin)
```

_**NOTE**_: _all translated fields in fields tuple will be changed to field+language_name 
(e.g.: `fields = ('name_ru', 'name_en', 'text_ru', 'text_en', 'info')`), and in admin form you will get
these fields instead of name, text etc_.

5. Now you are able to add some instance to a database, including translated fields. After that, when you call
`BasicModel.objects.first().name`, you will get a result **depending on your language**
   
## More information here

- https://django-modeltranslation.readthedocs.io/en/latest/installation.html
- https://phrase.com/blog/posts/quick-guide-django-i18n/
