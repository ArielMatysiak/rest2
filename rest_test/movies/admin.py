from django.contrib import admin
from movies.models import Movie, Person, RoleInfo
# Register your models here.

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(RoleInfo)