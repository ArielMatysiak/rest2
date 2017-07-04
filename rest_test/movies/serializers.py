from .models import Movie, Person, RoleInfo
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    actors = PersonSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('director', 'actors')
