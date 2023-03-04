from django.contrib import admin
from .models import *

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'room_price','room_description']

admin.site.register(Tag)
admin.site.register(Room , RoomAdmin)
admin.site.register(Room_images)

# Register your models here.
