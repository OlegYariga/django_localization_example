from django.contrib import admin
from django.urls import path
from project.views import ExampleView


urlpatterns = [
    path('', ExampleView.as_view()),
    path('admin/', admin.site.urls),
]
