from django.conf.urls import url
from games import views

urlpatterns = [
    url('esrb-ratings/',views.EsrbRatingList.as_view(), name=views.EsrbRatingList.name),
    url('esrb-ratings/<int:pk>/', views.EsrbRatingDetail.as_view(), name=views.EsrbRatingDetail.name),
    url('games/', views.GameList.as_view(), name=views.GameList.name),
    url('games/<int:pk>/', views.GameDetail.as_view(), name=views.GameDetail.name),
    url('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
    url('players/<int:pk>/', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    url('player-scores/', views.PlayerScoreList.as_view(), name=views.PlayerScoreList.name),
    url('player-scores/<int:pk>/', views.PlayerScoreDetail.as_view(), name=views.PlayerScoreDetail.name),
    url('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]