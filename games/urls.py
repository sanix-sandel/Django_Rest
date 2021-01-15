from django.conf.urls import url
from games import views

urlpatterns = [
    url('games', views.game_collection),
    url('games/<int:id>', views.game_detail),
]