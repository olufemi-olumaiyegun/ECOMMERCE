from django.contrib import admin
from .models import Item
# Register your models here.
@admin.register(Item)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'price', 'delivery_time']
    fields = ['title','description', 'price', 'delivery_time','picture']