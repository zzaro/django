from django.contrib import admin
from members.models import Members


# Register your models here.
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'tel', 'address')