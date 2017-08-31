from django.conf.urls import url
from . import views

app_name='music'
urlpatterns = [
    # /music/
    # url(r'^$', views.index , name='index'),

    #/music/71  here 71 is the album id we pass it using get method
    # url(r'^(?P<album_id>[0-9]+)/$' , views.detail , name='details'),

    #/music/<album_id>/favourite/
    # url(r'^(?P<album_id>[0-9]+)/favourite$' , views.favourite , name='favourite'),

    # /music/
    url(r'^$', views.IndexView.as_view() , name='index'),

    #/music/<album_id>/favourite/
    url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name='details'),

]
