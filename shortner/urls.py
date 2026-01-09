from django.urls import path

from . import views

app_name = "shortner"

urlpatterns = [
    path("<slug:code>/", views.follow_short_url, name="redirect"),
]