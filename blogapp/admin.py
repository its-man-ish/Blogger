from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('author','title','body')

admin.site.register(Category)

admin.site.register(UserProfile)

admin.site.register(Comments)