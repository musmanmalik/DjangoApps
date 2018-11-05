from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
    #default url
    path('', views.IndexView.as_view(), name='index'),
    #path('/<pk>', views.IndexView.as_view(), name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('forgot_password/', views.Forgot_Password.as_view(), name='forgot_password'),
    path('add_song/<album_id>', views.Add_Song.as_view(), name='add_song'),
    path('verify/', views.Verify.as_view(), name='verify'),
   # path('add_song/<pk>', views.Add_Song.as_view(), name='add_song'),
    #path('add_song/<pk>', views.Add_Song.as_view(), name='add_song'),
    path('music/index1', views.index1, name='index1'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.LoginView.as_view(), name='login'),
    path('music/contact', views.ContactView.as_view(), name='contact'),
    #music/album/add
    path('album/add', views.AlbumCreate.as_view(), name='album-add'),
    path('album/<pk>', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),
    path('<int:album_id>/',views.detail, name='detail'),
#    path('downloadSong/', views.downloadSong, name= 'song')
#    path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]
