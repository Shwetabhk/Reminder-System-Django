from django.contrib import admin
from .models import Company,Truck,Notification
# Register your models here.
admin.site.register(Company)
admin.site.register(Truck)
admin.site.register(Notification)