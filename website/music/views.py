# from django.http import Http404
# from django.http import HttpResponse
# from django.shortcuts import render , get_object_or_404
# from .models import Album,Song
#
# # Create your views here.
# def index(request):
#     all_albums=Album.objects.all()
#     context={
#         'all_albums':all_albums,
#     }
#     return render(request , "music/index.html" , context)
#
# def detail(request , album_id):
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exists")
#     album=get_object_or_404(Album , pk=album_id) #same as try except commented above
#     context={
#         'album':album
#     }
#     return render(request,"music/details.html",context)
#
# def favourite(request , album_id):
#     album=get_object_or_404(Album , pk=album_id)
#     context={
#     'error_message':"You did not select the right song",
#     'album':album
#     }
#     try:
#         selected_song=album.song_set.get(pk=request.POST['song'])
#
#     except(KeyError , Song.DoesNotExist):
#         return render(request,"music/details.html",context)
#
#     else:
#         # print selected_song
#         selected_song.is_favourite=True
#         selected_song.save()
#         return render(request,"music/details.html",{'album':album})

from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name="all_albums"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model=Album
    template_name="music/details.html"
