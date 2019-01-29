from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recommend', views.recommend, name='recommend'),
    url(r'^relate', views.recommend, name='relate'),
    url(r'^keyword', views.keyword, name='keyword'),
    url(r'^display', views.display, name='display'),
]
