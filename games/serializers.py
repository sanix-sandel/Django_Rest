from rest_framework import serializers
from games.models import*
import games.views
from django.contrib.auth.models import User

class EsrbRatingSerializer(serializers.HyperlinkedModelSerializer):
    games=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail'
    )

    class Meta:
        model=EsrbRating
        fields=(
            'url',
            'id',
            'description',
            'games'
        )


class GameSerializer(serializers.ModelSerializer):

    esrb_rating=serializers.SlugRelatedField(
        queryset=EsrbRating.objects.all(),
        slug_field='description'
    )
    owner=serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=Game
        fields=(
            'url',
            'name',
            'release_date',
            'esrb_rating',
            'played_once',
            'played_times',
            'played_times',
            'owner'
        )

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game=GameSerializer

    class Meta:
        model=PlayerScore
        fields=(
            'url',
            'id',
            'score',
            'score_date',
            'game'
        )        

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores=ScoreSerializer(many=True, read_only=True)
    gender=serializers.ChoiceField(
        choices=Player.GENDER_CHOICES
    )        
    gender_description=serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model=Player
        fields=(
            'url',
            'name',
            'gender',
            'gender_description',
            'scores'
        )


class PlayerScoreSerializer(serializers.ModelSerializer):
    player=serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    game=serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model=PlayerScore
        fields=(
            'url',
            'id',
            'score',
            'score_date',
            'player',
            'game'
        )

class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'url',
            'name'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'username',
            'games')       