from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Post



# Register your models here.

admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):

    model = User

    # Only display the "username" field

    fields = ["username"]
    inlines = [ProfileInline]

admin.site.register(User, UserAdmin) 

# admin.site.register(Profile)

admin.site.unregister(Group)

admin.site.register(Post)