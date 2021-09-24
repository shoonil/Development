from django.contrib import admin
from .models import Membership
# Register your models here.


# admin.site.register(Membership)
@admin.register(Membership)
class membershipModel(admin.ModelAdmin):
    list_filter=('FullName','CurrentAddress')
    list_display=('FullName', 'CurrentAddress')