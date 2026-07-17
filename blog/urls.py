from django.urls import path
from blog import views
from blog.views import BlogIndexView

app_name = "blog"

urlpatterns = [
    path("", BlogIndexView.as_view(), name="index"),
]
