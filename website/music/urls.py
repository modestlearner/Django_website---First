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

    #/music/album/add
    url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),

    #/music/album/pk
    url(r'^album/(?P<pk>[0-9]+)/$' , views. AlbumUpdate.as_view() , name='album-update'),

    #/music/album/pk/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$' , views.AlbumDelete.as_view() , name='album-delete'),

    #/music/register
    url(r'^register/$', views.UserFormView.as_view() , name='register'),



]
