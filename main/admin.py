from main.models import StoreInventory
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StoreInventory)
admin.site.register(Store)