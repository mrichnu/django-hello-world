from django.conf.urls import url
from hellocount import views

urlpatterns = [
    url(r'^$', views.say_hello, name='home'),
]
