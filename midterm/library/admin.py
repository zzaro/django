from django.contrib import admin
from library.models import Library


# Register your models here.
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher')