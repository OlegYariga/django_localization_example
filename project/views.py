from django.http import HttpResponse
from django.utils.translation import activate
from django.utils.translation import ugettext as _
from django.views import View

from project.localetest.models import BasicModel


class ExampleView(View):
    def get(self, request):
        request.LANGUAGE_CODE = request.GET.get('language', 'ru')
        activate(language=request.GET.get('language', 'ru'))

        # to translate some text, use ugettext or gettext
        some_text = _("Привет, мир!")

        # model results will be already translated here
        model_object = BasicModel.objects.first()

        return HttpResponse(
            f"text in code: {some_text}<br> text from database: {model_object.name} - {model_object.text}",
            status=200
        )
