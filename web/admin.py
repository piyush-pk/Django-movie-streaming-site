from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User

admin.site.site_header = "Movies Player Admin Panel"
admin.site.site_title = "Movies Player"

# Register your models here.
class moviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'rating', 'time')

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Category')

admin.site.register(Movies, moviesAdmin)
admin.site.register(Category, categoryAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)