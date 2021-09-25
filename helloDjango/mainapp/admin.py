from django.contrib import admin
from mainapp.models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')


class CateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num')


class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'price', 'category')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id_','name','city','address','store_type','logo')
    fields = ('name','city','address','store_type','logo','summary')

admin.site.register(UserEntity, UserAdmin)
admin.site.register(CateTypeEntity,CateTypeAdmin)
admin.site.register(FruitEntity,FruitAdmin)
admin.site.register(StoreEntity,StoreAdmin)
