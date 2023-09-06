from django.contrib import admin

from userapp.models import Profile


# Register your models here.


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    model = Profile
