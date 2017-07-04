from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name="film_director")
    actors = models.ManyToManyField(Person, through="RoleInfo")
    year = models.SmallIntegerField()

    def __str__(self):
        return self.title


class RoleInfo(models.Model):
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    info = models.CharField(max_length=124)

    def __str__(self):
        return self.info






